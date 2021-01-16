import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import time
import os

def makeittalk(text):
    window = Tk()

    image = Image.open('cloud_idle.gif')
    tk_image = ImageTk.PhotoImage(image)
    image2 = Image.open('speech_bubble.png')
    tk_image2 = ImageTk.PhotoImage(image2)

    cloudgif = tk.Label(window, image=tk_image, compound='center', bg='black')

    speechbubble = tk.Label(window, text=text, image=tk_image2, compound='center', bg='black')
    speechbubble.config(font=("Courier 10 bold"))

    window.overrideredirect(True) #remove the window border

    window.wm_attributes('-transparentcolor', 'black')

    cloudgif.pack()
    speechbubble.pack()
    window.mainloop()

makeittalk('Hi bitchhh')