from tkinter import *
import time
import os

x=1400
root = Tk()

frameCnt = 5
frames = [PhotoImage(file='idle.gif', format='gif -index %i' % (i)) for i in range(frameCnt)]


def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(100, update, ind)
    root.geometry('100x100+' + str(x) + '+900')


root.config(highlightbackground='black')
# make movable and show animation
label = Label(root, bd=0, bg='black')
root.overrideredirect(True)
# make  pet background from black to transparent
root.wm_attributes('-transparentcolor', 'black')
root.wm_attributes("-topmost", 1)
label.pack()
root.after(0, update, 0)
root.mainloop()
