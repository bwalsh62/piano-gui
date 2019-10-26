# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 20:12:40 2019
Last updated October 26 2019

@author: Ben Walsh
for liloquy

TO DO
----
- Add string instrument for keyboard
- Change/remove numeric ticks for chords
- Add Key entry (D for F#, etc.)
- Adjust volume so background music is softer
-- Eventually have slider for adjustable volumes
- Add +/- to adjust bpm
"""

#%% Import libraries
# GUI with tkinter
from tkinter import Tk, Label, Button, Scale, Frame, Entry, PhotoImage
# Numerical processing with numpy
import numpy as np
# Music player from pygame
from pygame import mixer
# Custom piano sound functions
from piano_notes import sound_C, sound_Csharp, sound_D, sound_Dsharp, sound_E, sound_F, sound_Fsharp, sound_G, sound_Gsharp, sound_A, sound_Asharp, sound_B
# Custom music function for making melody
from melody import make_melody

#%% Initialize GUI

root = Tk()
root.title('liloquy: piano chords')
root.geometry('{}x{}'.format(360, 440))

# Create main frame containers
top_frame = Frame(root, bg='blue', width=360, height=400, pady=2)
btm_frame = Frame(root, bg='white', width=360, height=200, padx=2, pady=2)

# Initialize music mixer
mixer.init()

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ew")
btm_frame.grid(row=1, sticky="ew")

#%% Define functions for playing chords

sounds = [sound_C,sound_D,sound_E,sound_F,sound_G,sound_A,sound_B]

def chords_repeat():
    
    # Get input entry for bpm
    if bpm_entry.get().isdigit():
        bpm = int(bpm_entry.get())
    else:
        bpm = 60
        print('Invalid entry: '+bpm_entry.get()+', using '+str(bpm)+' for bpm')  
    
    # Top-line melody
    mel1_wav_name = './mel1.wav'
    note_num1 = chord1_scale.get()   
    note_num2 = chord2_scale.get()   
    note_num3 = chord3_scale.get()   
    note_num4 = chord4_scale.get()
    mel_array=np.array([note_num1,note_num2,note_num3,note_num4])
    mel1_wav_name = make_melody(mel1_wav_name,note_num1,note_num2,note_num3,note_num4,bpm)
    #mel1_wav_name = make_melody(mel1_wav_name,mel_array,bpm)

    mel2_wav_name = './mel2.wav'
    note_num1 = (note_num1+2)%7  
    note_num2 = (note_num2+2)%7  
    note_num3 = (note_num3+2)%7   
    note_num4 = (note_num4+2)%7
    mel2_wav_name = make_melody(mel2_wav_name,note_num1,note_num2,note_num3,note_num4,bpm)
    #mel2_wav_name = make_melody(mel2_wav_name,(mel_array+2)%7,bpm)

    mel3_wav_name = './mel3.wav'
    note_num1 = (note_num1+2)%7  
    note_num2 = (note_num2+2)%7  
    note_num3 = (note_num3+2)%7   
    note_num4 = (note_num4+2)%7
    mel3_wav_name = make_melody(mel3_wav_name,note_num1,note_num2,note_num3,note_num4,bpm)
    #mel3_wav_name = make_melody(mel3_wav_name,(mel_array+4)%7,bpm)

    melody1 = mixer.Sound(mel1_wav_name)
    melody2 = mixer.Sound(mel2_wav_name)
    melody3 = mixer.Sound(mel3_wav_name)

    # Get input entry for # of times to repeat
    if rpt_entry.get().isdigit():
        n_repeats = int(rpt_entry.get())
    else:
        n_repeats=1
        print('Invalid entry: '+rpt_entry.get()+', using '+str(n_repeats)+' for # loops')    
    melody1.play(n_repeats)
    melody2.play(n_repeats)
    melody3.play(n_repeats)
 
#%% Define sliders for Chords
        
chords = ['C','D','E','F','G','A','B']

# Label
lbl = Label(top_frame, text="Chords:", font=("Arial", 12),bg='Blue')
lbl.grid(columnspan=4, row=0, sticky="W")

# For testing, display the value of each slider
def chord_show():
    lbl.configure(text="Chords: "+chords[chord1_scale.get()] + " " \
                                 +chords[chord2_scale.get()] + " " \
                                 +chords[chord3_scale.get()] + " " \
                                 +chords[chord4_scale.get()])

chord1_scale = Scale(top_frame,from_=0,to=6,bg='Purple')#, command=chord_show)
chord1_scale.grid(column=1,row=1)

chord2_scale = Scale(top_frame,from_=0,to=6,bg='Purple')#, command=chord_show)
chord2_scale.grid(column=2,row=1)

chord3_scale = Scale(top_frame,from_=0,to=6,bg='Purple')#, command=chord_show)
chord3_scale.grid(column=3,row=1)

chord4_scale = Scale(top_frame,from_=0,to=6,bg='Purple')#, command=chord_show)
chord4_scale.grid(column=4,row=1)

# Display chords for testing
show_chord_btn = Button(top_frame, width=12, height=1, text="Update chords", command=chord_show)
show_chord_btn.grid(column=4,columnspan=2, row=0)

# Play/Loop chords

# Picture for play button
photo = PhotoImage(file = r"C:\Users\benja\Documents\Liloquy\Marketing\PlayIconNoBorder.png") 
# Resizing image to fit on button 
play_img = photo.subsample(6) 

play_chord_btn = Button(top_frame, width=34, text="Play", command=chords_repeat, image=play_img)
play_chord_btn.grid(column=1,row=2)

# Stop chords

# Picture for stop button
photo = PhotoImage(file = r"C:\Users\benja\Documents\Liloquy\Marketing\StopIconNoBorder.png") 
# Resizing image to fit on button 
stop_img = photo.subsample(6) 

# Button to stop
stop_btn = Button(top_frame, width=34,text="Stop",command=mixer.stop, image=stop_img)
stop_btn.grid(column=2,row=2)

# Number of repeats
#------------------
# Repeat # Label
rpt_lbl = Label(top_frame, text="Repeats:", font=("Arial", 10),bg='Blue')
rpt_lbl.grid(column=4, row=2, sticky="W")

# Repeat # Entry
rpt_entry = Entry(top_frame, width=5)
rpt_entry.grid(column=5,row=2)

# Initialize Entry with default loops = 2 
rpt_entry.insert(0,'2')

# Tempo in BPM
#-----------------
# BPM Label
bpm_lbl = Label(top_frame, text="BPM:", font=("Arial", 10),bg='Blue')
bpm_lbl.grid(column=6, row=2, sticky="W")

# Repeat # Entry
bpm_entry = Entry(top_frame, width=5)
bpm_entry.grid(column=7,row=2)

# Initialize Entry with default bpm = 60 
bpm_entry.insert(0,'60')

#%% Define buttons for piano keys
bkey_row = 3
wkey_row = 4

key_width = 5
key_height = 8

# C# key
Csharp_btn = Button(btm_frame, width=key_width, height=key_height, text="C#", command=sound_Csharp.play, bg="black", fg="white")
Csharp_btn.grid(column=1, columnspan=2,row=bkey_row)

# Dsharp key
Dsharp_btn = Button(btm_frame, width=key_width, height=key_height, text="D#", command=sound_Dsharp.play, bg="black", fg="white")
Dsharp_btn.grid(column=3, columnspan=2,row=bkey_row)

# Fsharp key
Fsharp_btn = Button(btm_frame, width=key_width, height=key_height, text="F#", command=sound_Fsharp.play, bg="black", fg="white")
Fsharp_btn.grid(column=7, columnspan=2,row=bkey_row)

# Gsharp key
Gsharp_btn = Button(btm_frame, width=key_width, height=key_height, text="G#", command=sound_Gsharp.play, bg="black", fg="white")
Gsharp_btn.grid(column=9, columnspan=2,row=bkey_row)

# Asharp key
Asharp_btn = Button(btm_frame, width=key_width, height=key_height, text="A#", command=sound_Asharp.play, bg="black", fg="white")
Asharp_btn.grid(column=11, columnspan=2,row=bkey_row)

# C key
C_btn = Button(btm_frame, width=key_width, height=key_height, text="C", command=sound_C.play, bg="white", fg="black")
C_btn.grid(column=0, columnspan=2, row=wkey_row)

# D key
D_btn = Button(btm_frame, width=key_width, height=key_height, text="D", command=sound_D.play, bg="white", fg="black")
D_btn.grid(column=2, columnspan=2,row=wkey_row)

# E key
E_btn = Button(btm_frame, width=key_width, height=key_height, text="E", command=sound_E.play, bg="white", fg="black")
E_btn.grid(column=4, columnspan=2,row=wkey_row)

# F key
F_btn = Button(btm_frame, width=key_width, height=key_height, text="F", command=sound_F.play, bg="white", fg="black")
F_btn.grid(column=6, columnspan=2,row=wkey_row)

# G key
G_btn = Button(btm_frame, width=key_width, height=key_height, text="G", command=sound_G.play, bg="white", fg="black")
G_btn.grid(column=8, columnspan=2,row=wkey_row)

# A key
A_btn = Button(btm_frame, width=key_width, height=key_height, text="A", command=sound_A.play, bg="white", fg="black")
A_btn.grid(column=10, columnspan=2,row=wkey_row)

# B key
B_btn = Button(btm_frame, width=key_width, height=key_height, text="B", command=sound_B.play, bg="white", fg="black")
B_btn.grid(column=12, columnspan=2,row=wkey_row)
 
root.mainloop()