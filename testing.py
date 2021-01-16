import pyautogui
import random  # pet will move in random direction
import tkinter as tk  # used as GUI

# x position on screen
x = 1400
cycle = 0
# pet must be idling because we assigned variable ‘check’ is 1,
# after the .gif loops once, the ‘event_number‘ will randomly change btwn 1 to 9
# has a probability of:
# * 4/9 to keep idling or walking toward left and right
# * 1/9 chance to change from idle to sleeping
check = 1
idle_num = [1, 2, 3, 4]  # 5 is idle to sleep
# once gif changes to idle-to-sleep, it must perform a sleep action to prevent instant waking up which is unnatural
sleep_num = [10, 11, 12, 13, 15]  # 14 is sleep to idle
walk_left = [6, 7]
walk_right = [8, 9]
event_number = random.randrange(1, 3, 1)


# transfer random no. to event
def event(cycle, check, event_number, x):
    if event_number in idle_num:
        check = 0
        print('idle')
        window.after(400, update, cycle, check, event_number, x)  # no. 1,2,3,4 = idle
    elif event_number == 5:
        check = 1
        print('from idle to sleep')
        window.after(100, update, cycle, check, event_number, x)  # no. 5 = idle to sleep
    elif event_number in walk_left:
        check = 4
        print('walking towards left')
        window.after(100, update, cycle, check, event_number, x)  # no. 6,7 = walk towards left
    elif event_number in walk_right:
        check = 5
        print('walking towards right')
        window.after(100, update, cycle, check, event_number, x)  # no 8,9 = walk towards right
    elif event_number in sleep_num:
        check = 2
        print('sleep')
        window.after(1000, update, cycle, check, event_number, x)  # no. 10,11,12,13,15 = sleep
    elif event_number == 14:
        check = 3
        print('from sleep to idle')
        window.after(100, update, cycle, check, event_number, x)  # no. 15 = sleep to idle


# making gif work
# variable ‘cycle’ will increase by 1, but when > (length of the frame array - 1), decrements to 0
# and changes the event_number in randrange to have pet change actions every time a gif has looped once
def gif_work(cycle, frames, event_number, first_num, last_num):
    if cycle < len(frames) - 1:
        cycle += 1
    else:
        cycle = 0
        event_number = random.randrange(first_num, last_num + 1, 1)
    return cycle, event_number


# need our pet to do an action with assigning a number to every action
# (defines time probability of an action occuring)
def update(cycle, check, event_number, x):
    # idle
    if check == 0:
        frame = idle[cycle]
        cycle, event_number = gif_work(cycle, idle, event_number, 1, 9)
    # idle to sleep
    elif check == 1:
        frame = idle_to_sleep[cycle]
        cycle, event_number = gif_work(cycle, idle_to_sleep, event_number, 10, 10)  # sleep
    elif check == 2:
        frame = sleep[cycle]
        cycle, event_number = gif_work(cycle, sleep, event_number, 10, 15)  # sleep to idle
    elif check == 3:
        frame = sleep_to_idle[cycle]
        cycle, event_number = gif_work(cycle, sleep_to_idle, event_number, 1, 1)  # walk toward left
    elif check == 4:
        frame = walk_positive[cycle]
        cycle, event_number = gif_work(cycle, walk_positive, event_number, 1, 9)
        x -= 3  # walk towards right
    elif check == 5:
        frame = walk_negative[cycle]
        cycle, event_number = gif_work(cycle, walk_negative, event_number, 1, 9)
        x -= -3

    # location of our tkinter window aka the position of our pet:
    # ‘100x100’ is the size of our pet in pixel,
    # ‘x’ is the x position in our screen,
    # ‘1050’ is the floor our pet stepping on.(it change with the resolution of your screen)
    window.geometry('100x100+' + str(x) + '+1050')
    label.configure(image=frame)
    window.after(1, event, cycle, check, event_number, x)


# tkinter window where pet is placed
# PhotoImage() can only be called after creation of Tk()
window = tk.Tk()

# call buddy's action gif to an array
# PhotoImage() can only be called after creation of Tk()
idle = [tk.PhotoImage('idle.gif', format='gif -index %i' % (i)) for i in range(5)]  # idle gif
idle_to_sleep = [tk.PhotoImage('idle_to_sleep.gif', format='gif -index %i' % (i)) for i in range(8)]  # idle to sleep gif
sleep = [tk.PhotoImage('sleep.gif', format='gif -index %i' % (i)) for i in range(3)]  # sleep gif
sleep_to_idle = [tk.PhotoImage('sleep_to_idle.gif', format='gif -index %i' % (i)) for i in range(8)]  # sleep to idle gif
walk_positive = [tk.PhotoImage('walking_positive.gif', format='gif -index %i' % (i)) for i in range(8)]  # walk to left gif
walk_negative = [tk.PhotoImage('walking_negative.gif', format='gif -index %i' % (i)) for i in range(8)]  # walk to right gif

# window configuration
window.config(highlightbackground='black')
# make movable and show animation
label = tk.Label(window, bd=0, bg='black')
window.overrideredirect(True)
# make  pet background from black to transparent
window.wm_attributes('-transparentcolor', 'black')

# make movable and show animation
label.pack()

# loop the program
# program will call the update function with the following assignment after 1000 ms,
# which is 1s and we could control the speed of the animation by changing it.
window.after(1, update, cycle, check, event_number, x)

window.mainloop()