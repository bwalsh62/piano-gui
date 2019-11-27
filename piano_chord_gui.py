# -*- coding: utf-8 -*-
"""

Primary GUI to play piano along with a background chord progression
Run script to open GUI
Creates .wav files for generated chord progression
./mel1.wav, ./mel2.wav and ./mel3.wav 

Created on Mon Apr 22 20:12:40 2019
Last updated November 26 2019

@author: Ben Walsh
for liloquy

TO DO
----
- Add string instrument for keyboard
- Adjust volume so background music is softer
-- Eventually have slider for adjustable volumes
- Add +/- to adjust bpm
- Script to redefine sound_C etc when instrument changes 
- PyInstaller for application
- Bottom menu for settings, etc.
- Record/Liloquy button next to play/stop?
"""

#%% Import libraries

# GUI with tkinter
from tkinter import Tk, Label, Button, Scale, Frame, Entry, PhotoImage, ttk, OptionMenu, StringVar

# Numerical processing with numpy
import numpy as np

# Check files exist with os.path
import os.path

# Music player from pygame
from pygame import mixer

# Custom piano sound functions
from piano_notes import sound_dict

# Custom music function for making melody
from gui_functions import chords_repeat_func

#%% Initialize GUI

root = Tk()
root.title('liloquy: piano chords')
root.geometry('{}x{}'.format(325, 515))

# Create main frame containers
top_frame = Frame(root, bg='blue', width=340, height=400, pady=2)
piano_frame = Frame(root, bg='brown', width=340, height=500, padx=2, pady=2)
menu_frame = Frame(root, bg='gray', width=340, height=180, padx=2, pady=2)

# Tabbed interface 
#-------------------------------------
# Advanced: type bpm, adjust chords manually, ...
# Simple, +/- bpm, preset happy/sad chords, ...

tab_parent = ttk.Notebook(top_frame)

stdTab = ttk.Frame(tab_parent, width=30, height=80)
advTab = ttk.Frame(tab_parent, width=30, height=80)

tab_parent.add(stdTab, text="Standard")
tab_parent.add(advTab, text="Advanced")

tab_parent.grid(column=0,row=1,columnspan=3)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ew")
piano_frame.grid(row=1, sticky="ew")
menu_frame.grid(row=2, sticky="ew")

# Initialize music mixer
mixer.init()

chords_full = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

#%% Define functions for playing chords

def chords_repeat():
    
    min_bpm = 30
    max_bpm = 120
    
    # Get bpm from active tab
    tab_name = tab_parent.tab(tab_parent.select(), "text")
    #print('active tab = '+tab_name) # for debugging
    if tab_name == 'Standard':
        bpm_entry_input = bpm_entry
    if tab_name =='Advanced':
        bpm_entry_input = bpm_entry_adv
        
    # Get input entry for bpm
    if bpm_entry_input.get().isdigit():
        # Setting minimum bpm
        if int(bpm_entry_input.get())<min_bpm:
            print('BPM too low. Using '+str(min_bpm)+' for bpm')  
            bpm_entry_input.delete(0, 'end') 
            bpm_entry_input.insert(0, min_bpm)
        # Setting maximum bpm
        if int(bpm_entry_input.get())>max_bpm:
            print('BPM too high. Using '+str(max_bpm)+' for bpm')  
            bpm_entry_input.delete(0, 'end') 
            bpm_entry_input.insert(0, max_bpm)
        bpm = int(bpm_entry.get())
    else:
        bpm = 75
        print('Invalid entry: '+bpm_entry_input.get()+', using '+str(bpm)+' for bpm')  
        bpm_entry_input.delete(0, 'end') # this will delete everything inside the entry
        bpm_entry_input.insert(0, bpm)
        
    # Top-line melody
    note_num1 = chord1_scale.get()   
    note_num2 = chord2_scale.get()   
    note_num3 = chord3_scale.get()   
    note_num4 = chord4_scale.get()
    
    mel_array=np.array([note_num1,note_num2,note_num3,note_num4])

    # Get input entry for # of times to repeat
    # Note that loops sets the number of time it will repeat
    #  E.g. to play once, loops=0, to play twice, loops=1 ,etc.
    
    if tab_name =='Standard':
        # Hiding repeat # and just loop 'forever' in standard mode
        n_repeats = 100
    else:
        if rpt_entry.get().isdigit():
            if int(rpt_entry.get())==0:
                # Special case where setting to -1 repeats infinitely
                n_repeats = 0
            else:
                n_repeats = int(rpt_entry.get())-1
        else:
            n_repeats=0
            print('Invalid entry: '+rpt_entry.get()+', using '+str(n_repeats)+' for # loops')    
            rpt_entry.delete(0, 'end') # this will delete everything inside the entry
            rpt_entry.insert(0, n_repeats)
    
    key_constant = chords_full.index(keyVar.get()) # keyVar.get() = 'D' -> keyConst = 2
    
    chords_repeat_func(bpm, n_repeats, mel_array, key_constant)
 
#%% Define sliders for Chords
        
chords = ['C','D','E','F','G','A','B']
note_chord_map = [0,2,4,5,7,9,11]
minor_tag = ['','m','m','','','m','dim']

# Label for chord/slider 1
lbl1 = Label(advTab, text="C", font=("Arial", 12))#,bg='Blue')
lbl1.grid(column=1, row=0, sticky="W")

# Label for chord/slider 2
lbl2 = Label(advTab, text="C", font=("Arial", 12))#,bg='Blue')
lbl2.grid(column=2, row=0, sticky="W")

# Label for chord/slider 3
lbl3 = Label(advTab, text="C", font=("Arial", 12))#,bg='Blue')
lbl3.grid(column=3, row=0, sticky="W")

# Label for chord/slider 4
lbl4 = Label(advTab, text="C", font=("Arial", 12))#,bg='Blue')
lbl4.grid(column=4, row=0, sticky="W")

# Callback to update the value of each slider
def update_labels(self):
    keyConst = chords_full.index(keyVar.get()) # keyVar.get() = 'D' -> keyConst = 2
    lbl1.configure(text=chords_full[(keyConst+note_chord_map[chord1_scale.get()])%12]+minor_tag[chord1_scale.get()]) # keyVar.get()
    lbl2.configure(text=chords_full[(keyConst+note_chord_map[chord2_scale.get()])%12]+minor_tag[chord2_scale.get()])
    lbl3.configure(text=chords_full[(keyConst+note_chord_map[chord3_scale.get()])%12]+minor_tag[chord3_scale.get()])
    lbl4.configure(text=chords_full[(keyConst+note_chord_map[chord4_scale.get()])%12]+minor_tag[chord4_scale.get()])

# Callback to update the value of each slider for a theme preset of chords
def update_theme(self):
    themeVal = themeVar.get() # keyVar.get() = 'D' -> keyConst = 2
    
    if themeVal == 'Happy':
        # 1-5-6-4 e.g. C G Am F
        # BPM 75
        chord1_scale.set(0)
        chord2_scale.set(4)
        chord3_scale.set(5)
        chord4_scale.set(3)
        
        bpm_entry.delete(0, 'end') 
        bpm_entry.insert(0, 75)
        
    elif themeVal == 'Sad':
        # 6-2-3-6 e.g. Am Dm Em Am
        # BPM 50
        chord1_scale.set(5)
        chord2_scale.set(1)
        chord3_scale.set(2)
        chord4_scale.set(5)
        
        bpm_entry.delete(0, 'end') 
        bpm_entry.insert(0, 55)
    
    update_labels(self)

# Define sliders for each chord
chord1_scale = Scale(advTab,from_=0,to=6,bg='Purple',command=update_labels,showvalue=0)
chord1_scale.grid(column=1,row=1, rowspan=3)

chord2_scale = Scale(advTab,from_=0,to=6,bg='Purple',command=update_labels,showvalue=0)
chord2_scale.grid(column=2,row=1, rowspan=3)

chord3_scale = Scale(advTab,from_=0,to=6,bg='Purple',command=update_labels,showvalue=0)
chord3_scale.grid(column=3,row=1, rowspan=3)

chord4_scale = Scale(advTab,from_=0,to=6,bg='Purple',command=update_labels,showvalue=0)
chord4_scale.grid(column=4,row=1, rowspan=3)

# Play/Loop chords
#------------------

# Picture for play button
playFile = "./icons/PlayIcon.png"
if not(os.path.exists(playFile)):
    print('Cannot find: '+playFile)
    
photo = PhotoImage(file = playFile) 
# Resizing image to fit on button 
play_img = photo.subsample(6) 

play_chord_btn = Button(top_frame, width=36, height=36,text="Play", command=chords_repeat, image=play_img)
play_chord_btn.grid(column=0,row=2)

# Stop chords
#------------------

# Picture for stop button
stopFile = "./icons/StopIcon.png"
photo = PhotoImage(file = stopFile) 
# Resizing image to fit on button 
stop_img = photo.subsample(6) 

# Button to stop
stop_btn = Button(top_frame, width=36,height=36, text="Stop",command=mixer.stop, image=stop_img)
stop_btn.grid(column=1,row=2)

# Number of repeats
#------------------
# Repeat # Label
rpt_lbl = Label(advTab, text="Repeats:", font=("Arial", 10))#,bg='Blue')
rpt_lbl.grid(column=6, row=3, sticky="W")

# Repeat # Entry
rpt_entry = Entry(advTab, width=5)
rpt_entry.grid(column=7,row=3)

# Initialize Entry with default loops = 2 
rpt_entry.insert(0,'2')

# Tempo in BPM
#-----------------
# BPM Label
bpm_lbl = Label(stdTab, text="BPM:", font=("Arial", 10))#,bg='Blue')
bpm_lbl.grid(column=6, row=1, sticky="W")
bpm_lbl2 = Label(advTab, text="BPM:", font=("Arial", 10))#,bg='Blue')
bpm_lbl2.grid(column=6, row=1, sticky="W")

# BPM Entries
bpm_entry = Entry(stdTab, width=5)
bpm_entry.grid(column=7,row=1)
bpm_entry_adv = Entry(advTab, width=5)
bpm_entry_adv.grid(column=7,row=1)

# Initialize Entry with default bpm = 75
bpm_entry.insert(0,'75')
bpm_entry_adv.insert(0,'75')

# Preset themes/chords for Basic/Standard
#-----------
theme_lbl = Label(stdTab, text="Theme:", font=("Arial",10))
theme_lbl.grid(column=6, row=3, sticky="W")
# Define list with keys
themeVar = StringVar(root)
themes = [ 'Happy','Sad']
themeVar.set(themes[0]) # set the default option

chooseThemeMenu = OptionMenu(stdTab, themeVar, *themes,command=update_theme)
chooseThemeMenu.grid(column=7, row=3, sticky="W")

# Major key
#-----------
key_lbl = Label(advTab, text="Key:", font=("Arial",10))
key_lbl.grid(column=6, row=2, sticky="W")
# Define list with keys
keyVar = StringVar(root)
keys = [ 'C','D','E','F','G','A','B']
keyVar.set(keys[0]) # set the default option

choosekeyMenu = OptionMenu(advTab, keyVar, *keys,command=update_labels)
choosekeyMenu.grid(column=7, row=2, sticky="W")

#%% Define buttons for piano keys to play asynchronously over background chords
bkey_row = 3
wkey_row = 4

key_width = 5
key_height = 8

# C# key
Csharp_btn = Button(piano_frame, width=key_width, height=key_height, text="C#", command=sound_dict['C#4'].play, bg="black", fg="white")
Csharp_btn.grid(column=1, columnspan=2,row=bkey_row)

# Dsharp key
Dsharp_btn = Button(piano_frame, width=key_width, height=key_height, text="D#", command=sound_dict['D#4'].play, bg="black", fg="white")
Dsharp_btn.grid(column=3, columnspan=2,row=bkey_row)

# Fsharp key
Fsharp_btn = Button(piano_frame, width=key_width, height=key_height, text="F#", command=sound_dict['F#4'].play, bg="black", fg="white")
Fsharp_btn.grid(column=7, columnspan=2,row=bkey_row)

# Gsharp key
Gsharp_btn = Button(piano_frame, width=key_width, height=key_height, text="G#", command=sound_dict['G#4'].play, bg="black", fg="white")
Gsharp_btn.grid(column=9, columnspan=2,row=bkey_row)

# Asharp key
Asharp_btn = Button(piano_frame, width=key_width, height=key_height, text="A#", command=sound_dict['A#4'].play, bg="black", fg="white")
Asharp_btn.grid(column=11, columnspan=2,row=bkey_row)

# C key
C_btn = Button(piano_frame, width=key_width, height=key_height, text="C", command=sound_dict['C4'].play, bg="white", fg="black")
C_btn.grid(column=0, columnspan=2, row=wkey_row)

# D key
D_btn = Button(piano_frame, width=key_width, height=key_height, text="D", command=sound_dict['D4'].play, bg="white", fg="black")
D_btn.grid(column=2, columnspan=2,row=wkey_row)

# E key
E_btn = Button(piano_frame, width=key_width, height=key_height, text="E", command=sound_dict['E4'].play, bg="white", fg="black")
E_btn.grid(column=4, columnspan=2,row=wkey_row)

# F key
F_btn = Button(piano_frame, width=key_width, height=key_height, text="F", command=sound_dict['F4'].play, bg="white", fg="black")
F_btn.grid(column=6, columnspan=2,row=wkey_row)

# G key
G_btn = Button(piano_frame, width=key_width, height=key_height, text="G", command=sound_dict['G4'].play, bg="white", fg="black")
G_btn.grid(column=8, columnspan=2,row=wkey_row)

# A key
A_btn = Button(piano_frame, width=key_width, height=key_height, text="A", command=sound_dict['A4'].play, bg="white", fg="black")
A_btn.grid(column=10, columnspan=2,row=wkey_row)

# B key
B_btn = Button(piano_frame, width=key_width, height=key_height, text="B", command=sound_dict['B4'].play, bg="white", fg="black")
B_btn.grid(column=12, columnspan=2,row=wkey_row)

#%% Main menu at bottom

# Picture for create option in menu
create_icon_file = r".\icons\Menu_CreateIcon.png"
photo = PhotoImage(file = create_icon_file) 
# Resizing image to fit on button 
create_menu_img = photo.subsample(7) 

# Button to choose Create option
create_btn = Button(menu_frame, width=36,height=36, image=create_menu_img)
create_btn.grid(column=1,row=wkey_row+1)

# Picture for listen option in menu
listen_icon_file = r".\icons\Menu_ListenIcon.png"
photo = PhotoImage(file = listen_icon_file) 
# Resizing image to fit on button 
listen_menu_img = photo.subsample(6) 

# Button to choose Listen option
listen_btn = Button(menu_frame, width=36,height=36, image=listen_menu_img)
listen_btn.grid(column=2,row=wkey_row+1)

#%% Run GUI
root.mainloop()