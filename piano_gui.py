# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 20:12:40 2019

@author: benja

TO DO
----
- Download recorded sounds for remaining flat keys
"""

#%% Import libraries
# GUI with tkinter
from tkinter import Tk, Label, Button
# Music player from pygame
from pygame import mixer
# Custom piano sound functions
from piano_notes import sound_C, sound_Csharp, sound_D, sound_Dsharp, sound_E, sound_F, sound_Fsharp, sound_G, sound_Gsharp, sound_A, sound_Asharp, sound_B

#%% Initialize GUI
window = Tk()

# Set title
window.title("Piano")

# Set default size
window.geometry('400x300')

# Label
lbl = Label(window, text="Note:", font=("Arial", 12))
lbl.grid(columnspan=4, row=0)

mixer.init()

#%% Define functions for pressing keys
def C_played():
    lbl.configure(text="Note: C")
    sound_C.play()
    
def Csharp_played():
    lbl.configure(text="Note: C#")
    sound_Csharp.play()
    
def D_played():
    lbl.configure(text="Note: D")
    sound_D.play()
    
def Dsharp_played():
    lbl.configure(text="Note: D#")
    sound_Dsharp.play()
    
def E_played():
    lbl.configure(text="Note: E")
    sound_E.play()
    
def F_played():
    lbl.configure(text="Note: F")
    sound_F.play() 
    
def Fsharp_played():
    lbl.configure(text="Note: F#")
    sound_Fsharp.play()
    
def G_played():
    lbl.configure(text="Note: G")
    sound_G.play() 

def Gsharp_played():
    lbl.configure(text="Note: G#")
    sound_Gsharp.play()
    
def A_played():
    lbl.configure(text="Note: A")
    sound_A.play() 

def Asharp_played():
    lbl.configure(text="Note: A#")
    sound_Asharp.play()
    
def B_played():
    lbl.configure(text="Note: B")
    sound_B.play() 

#%% Define buttons for piano keys
    
bkey_row = 2
wkey_row = 3

key_width = 5
key_height = 8

# C# key
Csharp_btn = Button(window, width=key_width, height=key_height, text="C#", command=Csharp_played, bg="black", fg="white")
Csharp_btn.grid(column=1, columnspan=2,row=bkey_row)

# Dsharp key
Dsharp_btn = Button(window, width=key_width, height=key_height, text="D#", command=Dsharp_played, bg="black", fg="white")
Dsharp_btn.grid(column=3, columnspan=2,row=bkey_row)

# Fsharp key
Fsharp_btn = Button(window, width=key_width, height=key_height, text="F#", command=Fsharp_played, bg="black", fg="white")
Fsharp_btn.grid(column=7, columnspan=2,row=bkey_row)

# Gsharp key
Gsharp_btn = Button(window, width=key_width, height=key_height, text="G#", command=Gsharp_played, bg="black", fg="white")
Gsharp_btn.grid(column=9, columnspan=2,row=bkey_row)

# Asharp key
Asharp_btn = Button(window, width=key_width, height=key_height, text="A#", command=Asharp_played, bg="black", fg="white")
Asharp_btn.grid(column=11, columnspan=2,row=bkey_row)

# C key
C_btn = Button(window, width=key_width, height=key_height, text="C", command=C_played, bg="white", fg="black")
C_btn.grid(column=0, columnspan=2, row=wkey_row)

# D key
D_btn = Button(window, width=key_width, height=key_height, text="D", command=D_played, bg="white", fg="black")
D_btn.grid(column=2, columnspan=2,row=wkey_row)

# E key
E_btn = Button(window, width=key_width, height=key_height, text="E", command=E_played, bg="white", fg="black")
E_btn.grid(column=4, columnspan=2,row=wkey_row)

# F key
F_btn = Button(window, width=key_width, height=key_height, text="F", command=F_played, bg="white", fg="black")
F_btn.grid(column=6, columnspan=2,row=wkey_row)

# G key
G_btn = Button(window, width=key_width, height=key_height, text="G", command=G_played, bg="white", fg="black")
G_btn.grid(column=8, columnspan=2,row=wkey_row)

# A key
A_btn = Button(window, width=key_width, height=key_height, text="A", command=A_played, bg="white", fg="black")
A_btn.grid(column=10, columnspan=2,row=wkey_row)

# B key
B_btn = Button(window, width=key_width, height=key_height, text="B", command=B_played, bg="white", fg="black")
B_btn.grid(column=12, columnspan=2,row=wkey_row)
 
window.mainloop()