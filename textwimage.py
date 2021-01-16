import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import time
import os

window = Tk()

#frameCnt = 5
#frames = [PhotoImage(file='idle.gif', format='gif -index %i' % (i)) for i in range(frameCnt)]


image = Image.open('speech_bubble.png')
tk_image = ImageTk.PhotoImage(image)

#cloudgif = 

speechbubble = tk.Label(window, text='Have a nice day!', image=tk_image, compound='center', bd=0)
speechbubble.config(font=("Courier 10 bold"))

window.overrideredirect(True) #remove the window border

window.wm_attributes('-transparentcolor', 'black')

speechbubble.pack()

window.mainloop()