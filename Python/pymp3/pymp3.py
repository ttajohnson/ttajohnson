# Import libraries
from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog

def addsongs():
    temp_song=filedialog.askopenfilenames(initialdir="Music/", title="Choose a song", filetypes=(("mp3 Files", "*.mp3"), ("wav Files", "*.wav")))

# Create Root Window
root = Tk()
root.title('PyMP3')
# Initialize mixer
mixer.init()

# Listbox to contain songs
songs_list=Listbox(root, selectmode=SINGLE, bg="black", fg="white", font=('arial', 15), height=12, width=47, selectbackground="gray", selectforeground="black")
songs_list.grid(columnspan=9)

# Font definition
defined_font = font.Font(family='Helvetica')

# Play Button
play_button=Button(root, text='Play', width=7, command=Play)
play_button['font']=defined_font
play_button.grid(row=1, column=0)

# Pause
pause_button=Button(root, text='Pause', width=7, command=Pause)
pause_button['font']=defined_font
pause_button.grid(row=1, column=1)

# Stop
stop_button=Button(root,text='Stop', width=7, command=Stop)
stop_button['font']=defined_font
stop_button.grid(row=1, column=2)

# Resume
resume_button=Button(root,text='Resume', width=7, command=Resume)
resume_button['font']=defined_font
resume_button.grid(row=1, column=3)

# Previous Button
prev_button=Button(root, text='Prev', width=7, command=Previous)
prev_button['font']=defined_font
prev_button.grid(row=1, column=4)

# Next Button
next_button=Button(root, text='Next', width=7, command=Next)
next_button['font']=defined_font
next_button.grid(row=1, column=5)

# Menu
my_menu=Menu(root)
root.config(menu=my_menu)
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Menu",menu=add_song_menu)
add_song_menu.add_command(label="Add Songs", command=addsongs)
add_song_menu.add_command(label="Delete Song", command=deletesong)

mainloop()