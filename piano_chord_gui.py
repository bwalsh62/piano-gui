# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 20:12:40 2019
Last updated October 20 2019

@author: Ben Walsh

TO DO
----
- Change/remove numeric ticks for chords
- Add BPM entry
- Play chords in background
- Remove Csharp_played etc.
"""

#%% Import libraries
# GUI with tkinter
from tkinter import Tk, Label, Button, Scale, Frame
# Music player from pygame
from pygame import mixer
# Custom piano sound functions
from piano_notes import sound_C, sound_Csharp, sound_D, sound_Dsharp, sound_E, sound_F, sound_Fsharp, sound_G, sound_Gsharp, sound_A, sound_Asharp, sound_B

#%% Initialize GUI

root = Tk()
root.title('Piano Chords')
root.geometry('{}x{}'.format(360, 500))

# Create all of the main frame containers
top_frame = Frame(root, bg='blue', width=360, height=400, pady=2)
btm_frame = Frame(root, bg='white', width=360, height=200, padx=2, pady=2)

# Initialize music mixer
mixer.init()

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ew")
btm_frame.grid(row=1, sticky="ew")

#%% Define functions for pressing keys

sounds = [sound_C,sound_D,sound_E,sound_F,sound_G,sound_A,sound_B]

def Csharp_played():
    sound_Csharp.play()
    
def Dsharp_played():
    sound_Dsharp.play()
    
def Fsharp_played():
    sound_Fsharp.play()

def Gsharp_played():
    sound_Gsharp.play()

def Asharp_played():
    sound_Asharp.play()

# Play 3 note chord
def chord_played():
    note_num = chord1_scale.get()   
    sounds[note_num].play()
    sounds[(note_num+2)%7].play()
    sounds[(note_num+4)%7].play()
    
#%% Define sliders for Chords
        
chords = ['C','D','E','F','G','A','B']

# Label
lbl = Label(top_frame, text="Chord:", font=("Arial", 12))
lbl.grid(columnspan=4, row=0, sticky="W")

# For testing, display the value of each slider
def chord_show():
    lbl.configure(text="Chords: "+chords[chord1_scale.get()] + " " \
                                 +chords[chord2_scale.get()] + " " \
                                 +chords[chord3_scale.get()] + " " \
                                 +chords[chord4_scale.get()])

chord1_scale = Scale(top_frame,from_=0,to=6)#, command=chord_show)
chord1_scale.grid(column=1,row=1)

chord2_scale = Scale(top_frame,from_=0,to=6)#, command=chord_show)
chord2_scale.grid(column=2,row=1)

chord3_scale = Scale(top_frame,from_=0,to=6)#, command=chord_show)
chord3_scale.grid(column=3,row=1)

chord4_scale = Scale(top_frame,from_=0,to=6)#, command=chord_show)
chord4_scale.grid(column=4,row=1)

# Below should be automatic with call backs
chord_btn = Button(top_frame, width=12, height=1, text="Update chords", command=chord_show)
chord_btn.grid(columnspan=3,row=2)

# Play chord (chord 1 for testing)
play_chord1_btn = Button(top_frame, width=12, height=1, text="Play chord 1", command=chord_played)
play_chord1_btn.grid(column=5,row=2)

#%% Define buttons for piano keys
bkey_row = 3
wkey_row = 4

key_width = 5
key_height = 8

# C# key
Csharp_btn = Button(btm_frame, width=key_width, height=key_height, text="C#", command=Csharp_played, bg="black", fg="white")
Csharp_btn.grid(column=1, columnspan=2,row=bkey_row)

# Dsharp key
Dsharp_btn = Button(btm_frame, width=key_width, height=key_height, text="D#", command=Dsharp_played, bg="black", fg="white")
Dsharp_btn.grid(column=3, columnspan=2,row=bkey_row)

# Fsharp key
Fsharp_btn = Button(btm_frame, width=key_width, height=key_height, text="F#", command=Fsharp_played, bg="black", fg="white")
Fsharp_btn.grid(column=7, columnspan=2,row=bkey_row)

# Gsharp key
Gsharp_btn = Button(btm_frame, width=key_width, height=key_height, text="G#", command=Gsharp_played, bg="black", fg="white")
Gsharp_btn.grid(column=9, columnspan=2,row=bkey_row)

# Asharp key
Asharp_btn = Button(btm_frame, width=key_width, height=key_height, text="A#", command=Asharp_played, bg="black", fg="white")
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