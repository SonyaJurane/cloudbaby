speechbubble = tk.Label(window, text=text, image=tk_image2, compound='center', bg='black')
speechbubble.config(font=("Courier 10 bold"))

window.overrideredirect(True) #remove the window border

window.wm_attributes('-transparentcolor', 'black') #make black colour transparent

cloudgif.pack()
speechbubble.pack()