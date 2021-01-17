import pyautogui
from tkinter import *
import tkinter as tk
import random
import time
import os
from PIL import Image, ImageTk
import ctypes
root = Tk()

action = random.randrange(-5, 5)
# screen resolution
user32 = ctypes.windll.user32
max_x = user32.GetSystemMetrics(0)
max_y = user32.GetSystemMetrics(1)

# start x and y positions
x = max_x-400
y = max_y-200

def obtain_prompt():
    prompts = []
    try:
        new_file = open('Prompts', 'r')
    except:
        print("Error, file not found")
    else:
        prompts = new_file.read().splitlines()

    return random.choice(prompts)

choose_prompt = obtain_prompt()

frames = [PhotoImage(file='cloud_idle.gif',format = 'gif -index %i' %(i)) for i in range(28)]


def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == 28:
        ind = 0
    global action, x, y
    rand = random.randrange(0, 100)
    if rand < 3:
        action = 0
    elif rand < 6:
        action = random.randrange(-5,5)

    if action >= 0:
        if x + action < max_x - 200:
            x += action
    else:
        if x + action > max_x - max_x//3:
            x += action

    print(action)

    root.geometry('200x147+' + str(x) + '+' + str(y))
    label.configure(image=frame)
    root.after(100, update, ind)
    choose_prompt = obtain_prompt()


label = tk.Label(root, bg='black')
label.pack()
root.after(0, update, 0)

image = Image.open('speech_bubble.png')
speechbubble_image = ImageTk.PhotoImage(image)
speechbubble = tk.Label(root, text=choose_prompt, image=speechbubble_image, compound='center', bg='black')
speechbubble.config(font=("Courier 8 bold"))

root.overrideredirect(True) #remove the window border

root.wm_attributes('-transparentcolor', 'black') #make black colour transparent
root.wm_attributes("-topmost", -1)


speechbubble.pack()

root.mainloop()