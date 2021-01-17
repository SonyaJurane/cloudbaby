from tkinter import *
import tkinter as tk
import time
import os
from PIL import Image, ImageTk
root = Tk()


frames = [PhotoImage(file='cloud_idle.gif',format = 'gif -index %i' %(i)) for i in range(28)]

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == 28:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)

label = tk.Label(root, bg='black')
label.pack()
root.after(0, update, 0)

image = Image.open('speech_bubble.png')
speechbubble_image = ImageTk.PhotoImage(image)
speechbubble = tk.Label(root, text='text', image=speechbubble_image, compound='center', bg='black')
speechbubble.config(font=("Courier 10 bold"))

root.overrideredirect(True) #remove the window border

root.wm_attributes('-transparentcolor', 'black') #make black colour transparent


speechbubble.pack()

root.mainloop()