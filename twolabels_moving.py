"""
Cloud Baby
By: Emily Zhou, Patty Liu, Saba Memon, and Sonya Jurane

Bibliography

TheNobody. "Simple Facial Recognition Lock in Python." Medium, 19 Mar. 20202019, 
    medium.com/analytics-vidhya/simple-facial-recognition-lock-in-python-fc3bdb65f9e2.
"""

import pyautogui
from tkinter import *
import tkinter as tk
import random
import pygame
import time
import os
from PIL import Image, ImageTk
import ctypes
global change
root = Tk()

action = random.randrange(-5, 5)
# screen resolution
user32 = ctypes.windll.user32
max_x = user32.GetSystemMetrics(0)
max_y = user32.GetSystemMetrics(1)

# start x and y positions
x = max_x-400
y = max_y-200

pygame.mixer.init()

def obtain_prompt():
    prompts = []
    try:
        newfile = open("Prompts", "r")
    except:
        print("Error")
    else:
        prompts = newfile.read().splitlines()
    return random.choice(prompts)

choose_prompt = obtain_prompt()

frames = [PhotoImage(file='cloud_idle.gif',format = 'gif -index %i' %(i)) for i in range(28)]
frame2 = [PhotoImage(file='cloud_talk.gif',format = 'gif -index %i' %(i)) for i in range(28)]
frame3 = [PhotoImage(file='cloud_uwu.gif',format = 'gif -index %i' %(i)) for i in range(28)]
frame4 = [PhotoImage(file='cloud_o.gif',format = 'gif -index %i' %(i)) for i in range(28)]
frame5 = [PhotoImage(file='cloud_w.gif',format = 'gif -index %i' %(i)) for i in range(28)]

def moveWindow(event):
    global x, y
    root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))
    if event.y_root > 0 and event.y_root < (max_y - 147):
        y = event.y_root
    if event.x_root > 0 and event.x_root < (max_x - 200):
        x = event.x_root


root.bind("<B1-Motion>", moveWindow)


def click(event):
    pygame.mixer.music.load("pop.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=0)

root.bind("<Button-1>", click)


def update(ind, state):
    if ind == 0:
        i = random.randint(1, 100)
        if i < 60:
            state = frames
        elif 61 <= i < 70:
            state = frame2
        elif 71 <= i < 80:
            state = frame3
        elif 81 <= i < 90:
            state = frame4
        else:
            state = frame5
    frame = state[ind]
    ind += 1
    if ind == 28:
        ind = 0
    global action, x, y
    rand = random.randrange(0, 100)
    if rand < 3:
        action = 0
    elif rand < 6:
        action = random.randrange(-5, 5)

    if action >= 0:
        if x + action < max_x - 200:
            x += action
    else:
        if x + action > max_x - max_x//3:
            x += action

    root.geometry('201x130+' + str(x) + '+' + str(y))
    label.configure(image=frame)
    root.after(100, update, ind, state)


label = tk.Label(root, bg='black')
label.pack()
state = frames[0]
root.after(0, update, 0, state)

image = Image.open('speech_bubble2.png')
speechbubble_image = ImageTk.PhotoImage(image)
speechbubble = tk.Label(root, text=choose_prompt, image=speechbubble_image, compound='center', bg='black')
speechbubble.config(font=("Courier 8 bold"))
speechbubble.config(fg="#9280CF")

root.overrideredirect(True) #remove the window border

root.wm_attributes('-transparentcolor', 'black') #make black colour transparent
root.wm_attributes("-topmost", -1)


def SEND():
    pygame.mixer.music.load("pop.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=0)
    speechbubble.config(text=obtain_prompt())
    root.after(10000, SEND)


speechbubble.pack()
SEND()
root.mainloop()