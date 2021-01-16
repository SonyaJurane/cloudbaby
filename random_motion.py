import pyautogui
import random  # pet will move in random direction
from tkinter import *
import time
import ctypes
import PIL

window = Tk()
action = [random.randrange(-5, 5), random.randrange(-5,5)]

# screen resolution
user32 = ctypes.windll.user32
max_x = user32.GetSystemMetrics(0)
max_y = user32.GetSystemMetrics(1)

# start x and y positions
x = max_x-400
y = max_y-200

# boolean to determine if there is text
no_text = TRUE

frameCnt = 5
frames = [PhotoImage(file='idle.gif', format='gif -index %i' % (i)) for i in range(frameCnt)]


# update method that updates the pet
def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    update_position()
    label.configure(image=frame)
    window.after(200, update, ind)


def update_position():
    global action, x, y
    rand = random.randrange(0, 100)
    if no_text:
        if rand < 3:
            action = [0, 0]
        elif rand < 6:
            action = [random.randrange(-5, 5), random.randrange(-5, 5)]
        x += action[0]
        y += action[1]
        if x > max_x:
            x -= action[0]
            action[0] = -action[0]
        if y > max_y:
            y -= action[1]
            action[1] = -action[1]
    window.geometry('100x100+' + str(x) + '+' + str(y))


window.config(highlightbackground='black')
# make movable and show animation
label = Label(window, bd=0, bg='black')
window.overrideredirect(True)
# make  pet background from black to transparent
window.wm_attributes('-transparent', 'black')
window.wm_attributes("-topmost", 1)
label.pack()
window.after(0, update, 0)
window.mainloop()
