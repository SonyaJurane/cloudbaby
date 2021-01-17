import pyautogui
import random  # pet will move in random direction
import tkinter as tk  # used as GUI
from datetime import datetime
import ctypes
import PIL
from textwimage import makeittalk

makeittalk(300, 400, 'Hello!')
        
cycle = 1

check = 0
idle_num = [1, 2, 3, 4]
talk = [5, 6]
event_number = random.randrange(1, 3, 1)
currenttime = datetime.now().strftime("%H:%M:%S")
# starttime = 

action = [random.randrange(-5, 5), random.randrange(-5,5)]
# screen resolution
user32 = ctypes.windll.user32
max_x = user32.GetSystemMetrics(0)
max_y = user32.GetSystemMetrics(1)

# start x and y positions
x = max_x-400
y = max_y-200


# transfer random no. to event
def event(cycle, check, event_number, x):
    # print(event_number)
    if event_number < 5:
        check = 0
        # print('idle')
        window.after(100, update, cycle, check, event_number, x)
    else:
        check = 1
        # print('from idle to talk')
        

        #window.after(1000, update, cycle, check, event_number, x)
        


# making gif work
def gif_work(cycle, frames, event_number):
    # if it is in idle mode we want it to keep looping through those frames
    if check == 0:
        if cycle < len(frames) - 1:
            cycle += 1
        else:
            cycle = 0
            event_number = random.randrange(0, 100)
    # if it is talking we want it to keep talking
    else:
        if cycle == 5:
            cycle = 6
        else:
            cycle = 5
    return cycle, event_number


# need our pet to do an action with assigning a number to every action
# (defines time probability of an action occuring)
def update(cycle, check, event_number, x):
    # idle
    if check == 0:
        frame = idle[cycle]
        cycle, event_number = gif_work(cycle, idle, event_number)

        global action, y
        rand = random.randrange(0, 100)

        if rand < 3:
            action = [0, 0]
        elif rand < 6:
            action = [random.randrange(-5, 5), random.randrange(-5, 5)]
        x += action[0]
        y += action[1]
        if x > max_x:
            x -= action[0]
            action[0] = -action[0]
    # talking
    elif check == 1:
        frame = idle_to_talk[cycle]
        cycle, event_number = gif_work(cycle, idle_to_talk, event_number)

    window.geometry('200x80+' + str(x) + '+' + str(max_y-150))
    label.configure(image=frame)
    window.after(1, event, cycle, check, event_number, x)


# tkinter window where pet is placed
# PhotoImage() can only be called after creation of Tk()
window = tk.Tk()

# call buddy's action gif to an array
# PhotoImage() can only be called after creation of Tk()
idle = [tk.PhotoImage(file='cloud_idle.gif', format='gif -index %i' % (i)) for i in range(28)]  # idle gif
idle_to_talk = [tk.PhotoImage(file='cloud_talk.gif', format='gif -index %i' % (i)) for i in
                range(28)]  # talk gif

# window configuration
window.config(highlightbackground='black')
# make movable and show animation
label = tk.Label(window, bd=0, bg='black')
window.overrideredirect(True)
# make  pet background from black to transparent
window.wm_attributes('-transparent', 'black')
window.wm_attributes("-topmost", 1)

# make movable and show animation
label.pack()

# after 1000 ms (1s), program will call update() to change animation
window.after(1, update, cycle, check, event_number, x)

# run the Tkinter event loop
window.mainloop()
