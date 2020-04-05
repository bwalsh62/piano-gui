# -*- coding: utf-8 -*-
"""

Primary GUI to play piano along with a background chord progression
Run script to open GUI
Creates .wav files for generated chord progression
./mel1.wav, ./mel2.wav and ./mel3.wav 

Created on Mon Apr 22 20:12:40 2019
Last updated December 3 2019

@author: Ben Walsh
for liloquy

TO DO
----
- ml_utils integrate with submodule for feat_extract
- generalize location of pickle model

- Adjust volume so background music is softer
-- Eventually have slider for adjustable volumes
- PyInstaller for application
- Operationalize Record/Liloquy button 
    X Record 3 seconds and save
    X Estimate note
    X Play back note in piano
    - Play on top of background melody
- Add string instrument for keyboard
- Script to redefine sound_C etc when instrument changes 

# Use new music_dict from liloquy-git... separate from piano part?

[ ] Recorded hums input arg for num_notes - not 2x default
[ ] Get musicMixDict as input function, not repeat it

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
from piano_notes import music_dict, music_theme, freq_dict

# Custom music function for making melody
from gui_functions import mel_wav_write, record_music

from melody import make_melody

#--------
# All here and below should be separate from a submodule
#
# Update eventually to link up submodules from ML separately...
#
#from note-recognition.ml_utils import music_feat_extract
from ml_utils import music_feat_extract

# Pickle to load pre-trained model
import pickle

import matplotlib.pyplot as plt

#%% Define constants

# Music notes
chords_full = ('C','C#','D','D#','E','F','F#','G','G#','A','A#','B')

# Constants for beats per minute
min_bpm = 30
max_bpm = 120
default_bpm = 75

#%% Initialize GUI

root = Tk()
root.title('liloquy - find your song')
root.geometry('{}x{}'.format(325, 515))

# Create main frame containers
#------------

top_frame = Frame(root, bg='blue', width=500, height=400, pady=2)
piano_frame = Frame(root, bg='brown', width=500, height=500, padx=2, pady=2)
menu_frame = Frame(root, bg='gray', width=500, height=180, padx=2, pady=2)

# Tabbed interface to separate standard and advanced features
#------------

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
            
#%% Define bpm pre-processing function

def bpm_input_process():
    # Get input entry for bpm
    if bpm_entry.get().isdigit():
        # Setting minimum bpm
        if int(bpm_entry.get())<min_bpm:
            print('BPM too low. Using {} for bpm'.format(min_bpm)) 
            bpm_entry.delete(0, 'end') 
            bpm_entry.insert(0, min_bpm)
        # Setting maximum bpm
        if int(bpm_entry.get())>max_bpm:
            print('BPM too high. Using {} for bpm'.format(max_bpm))  
            bpm_entry.delete(0, 'end') 
            bpm_entry.insert(0, max_bpm)
        bpm = int(bpm_entry.get())
    else:
        bpm = default_bpm
        print('Invalid entry: {}, using {} for bpm'.format(bpm_entry.get(),bpm))  
        bpm_entry.delete(0, 'end') # clears entry
        bpm_entry.insert(0, bpm)
    return bpm
   
#%% Define functions for playing music - hummed melody and/or background chords

def play_music():
    
    bpm = bpm_input_process()
    
    # Retrieve which melody to play
    #-------------------------------
    
    # Should get this is as input
    musicMixDict = dict(
        {'Both':(True,True),
         'Background Only':(True,False),
         'Melody Only':(False,True)
        })
    
    music_mix_sel = musicMixVar.get()
    if musicMixDict.get(music_mix_sel) == None:
        print('No playback selected or unknown option')
    else:
        play_chords_sel, play_mel_sel = musicMixDict[music_mix_sel]
        print('Playing chords = {}, playing melody = {}'.format(play_chords_sel,play_mel_sel))
    
    # Base chords
    note_num1 = chord1_scale.get()   
    note_num2 = chord2_scale.get()   
    note_num3 = chord3_scale.get()   
    note_num4 = chord4_scale.get()
    
    mel_array=np.array([note_num1,note_num2,note_num3,note_num4])
    
    # TEST for class eventually
    #------------------------
    # play_music_obj = play_music_class(mel_array)
    # play_music_obj.bpm = bpm

    # Get input entry for # of times to repeat
    # Note that loops sets the number of time it will repeat
    #  E.g. to play once, loops=0, to play twice, loops=1 ,etc.
    
    tab_name = tab_parent.tab(tab_parent.select(), "text")
    
    if tab_name =='Standard':
        # Hiding repeat number and just loop 'forever' in standard mode
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
    
    # TEST for class eventually
    #------------------------
    # play_music_obj.n_repeats = n_repeats
    
    key_constant = chords_full.index(keyVar.get()) # keyVar.get() = 'D' -> keyConst = 2
    
    # TEST for class eventually
    #------------------------
    # play_music_obj.key = key
    
    # Eventually have volume constant input from GUI    
#    # Change volume with this? How does this work?
#    mixer.music.set_volume
    
    mel1_wav, mel2_wav, mel3_wav, hum_mel_wav = mel_wav_write(bpm, 
        mel_array, key_constant)

    melody1 = mixer.Sound(mel1_wav)
    melody2 = mixer.Sound(mel2_wav)
    melody3 = mixer.Sound(mel3_wav)
    hum_melody = mixer.Sound(hum_mel_wav)

    if play_chords_sel:
        melody1.play(loops=n_repeats)
        melody2.play(loops=n_repeats)
        melody3.play(loops=n_repeats)
    
    if play_mel_sel:
        hum_melody.play(loops=n_repeats)


    # TEST for class eventually
    #------------------------
    # play_music_obj.play()

#%% Define function for recording then transcribing music

# Load ML model
modelName = r"C:\Users\benja\OneDrive\Documents\Python\liloquy-git\note-recognition\model.sav"
loaded_model = pickle.load(open(modelName, 'rb'))

#
# Function to record a sound then transcribe to a melody in piano
# record_transcribe_music(note_len_time = 1,rec_notes_total = 3, fs = 44100)
#   Inputs:
#       - note_len_time: Length in seconds of (shortest) note
#       - rec_notes_total: Number of consecutive notes to record

def record_transcribe_music(note_len_time = 1,rec_notes_total = 3, fs = 44100):
            
    recorded_sound = record_music(rec_notes_total, note_len_time, fs)
    
    # Initialize matrix of hummed notes
    hum = np.empty((rec_notes_total,fs * note_len_time))
    
    # Take single channel
    # Assume that hum_length is recorded length divided by number of notes
    # Eventually generalize duration or detect end
    for note in range(rec_notes_total):
        hum[note,:] = recorded_sound[fs * note_len_time*note:fs * note_len_time*(note+1),1]
    
    plt.plot(hum[0,:])
    plt.show()
    
    X_feat = music_feat_extract(hum,fs,freq_dict)
    print(X_feat)
    
    predicted_notes = loaded_model.predict(X_feat)
    for note in predicted_notes:
        print("Predicted note: "+note)
    
    # Play piano at predicted sound
    music_dict(note).sound.play()
        
    # Hummed melody
    mel_hum_wav_name = './mel_hum.wav'
    
    bpm = bpm_input_process()
        
    mel_hum_wav_name = make_melody(mel_hum_wav_name,predicted_notes,bpm,mode="note_name",debug=0)

    return recorded_sound

#%% Define sliders for Chords
        
chords = ('C','D','E','F','G','A','B')
note_chord_map = (0,2,4,5,7,9,11)
minor_tag = ('','m','m','','','m','dim')

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
    lbl1.configure(text=chords_full[(keyConst+note_chord_map[chord1_scale.get()])%12]+minor_tag[chord1_scale.get()]) 
    lbl2.configure(text=chords_full[(keyConst+note_chord_map[chord2_scale.get()])%12]+minor_tag[chord2_scale.get()])
    lbl3.configure(text=chords_full[(keyConst+note_chord_map[chord3_scale.get()])%12]+minor_tag[chord3_scale.get()])
    lbl4.configure(text=chords_full[(keyConst+note_chord_map[chord4_scale.get()])%12]+minor_tag[chord4_scale.get()])

# Callback to update the value of each slider for a theme preset of chords
def update_theme(self):
    theme = music_theme(themeVar.get()) 
    chord1_scale.set(theme.chords[0])
    chord2_scale.set(theme.chords[1])
    chord3_scale.set(theme.chords[2])
    chord4_scale.set(theme.chords[3])
    
    bpm_entry.delete(0, 'end') 
    bpm_entry.insert(0, theme.bpm)
    
    update_labels(self)

# Callback to increase bpm with + sign
def increase_bpm():
    bpm_to_insert = min(int(bpm_entry.get())+5,max_bpm)
    bpm_entry.delete(0, 'end') 
    bpm_entry.insert(0, bpm_to_insert)

def decrease_bpm():
    bpm_to_insert = max(int(bpm_entry.get())-5,min_bpm)
    bpm_entry.delete(0, 'end') 
    bpm_entry.insert(0, bpm_to_insert)

# Define sliders for each chord
chord1_scale = Scale(advTab,from_=0,to=6,bg='Purple',command=update_labels,showvalue=0)
chord1_scale.grid(column=1,row=1, rowspan=3, padx=10)

chord2_scale = Scale(advTab,from_=0,to=6,bg='Purple',command=update_labels,showvalue=0)
chord2_scale.grid(column=2,row=1, rowspan=3, padx=10)

chord3_scale = Scale(advTab,from_=0,to=6,bg='Purple',command=update_labels,showvalue=0)
chord3_scale.grid(column=3,row=1, rowspan=3, padx=10)

chord4_scale = Scale(advTab,from_=0,to=6,bg='Purple',command=update_labels,showvalue=0)
chord4_scale.grid(column=4,row=1, rowspan=3, padx=10)

# Play/Loop chords
#------------------

# Picture for play button
playFile = "./icons/PlayIcon.png"
if not(os.path.exists(playFile)):
    print('Cannot find: '+playFile)
    
photo = PhotoImage(file = playFile) 
# Resizing image to fit on button 
play_img = photo.subsample(6) 

#play_chord_btn = Button(top_frame, width=36, height=36,text="Play", command=chords_repeat, image=play_img)
play_chord_btn = Button(top_frame, width=36, height=36,text="Play", command=play_music, image=play_img)

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

# Record/Transcribe
#------------------

# Picture for record button
recordFile = "./icons/RecordIcon.png"
photo = PhotoImage(file = recordFile) 
# Resizing image to fit on button 
record_img = photo.subsample(8) 

# Button to record and transcribe
record_transcribe_btn = Button(top_frame, width=36,height=36, image=record_img, command=record_transcribe_music)
record_transcribe_btn.grid(column=2,row=2)

# Record/Instruct
#------------------

# Picture for record speech command button
recordSpeechFile = "./icons/RecordSpeechIcon.png"
photo = PhotoImage(file = recordSpeechFile) 
# Resizing image to fit on button 
record_speech_img = photo.subsample(6) 

# Button to record and transcribe
speech_cmd_btn = Button(top_frame, width=36,height=36, image=record_speech_img, command=record_transcribe_music)
speech_cmd_btn.grid(column=3,row=2)


# Choose playback - background, melody, both
#--------------------------

# Define list with music mixing options
musicMixVar = StringVar(root)

musicMixDict = dict(
        {'Both':(1,1),
         'Background Only':(1,0),
         'Melody Only':(0,1)
        })
    
musicMixOptions = list(musicMixDict.keys())
musicMixVar.set(musicMixOptions[0]) # set the default option

chooseMixMenu = OptionMenu(top_frame, musicMixVar, *musicMixOptions)
chooseMixMenu.grid(column=0, row=3, columnspan=2)

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
bpm_entry = Entry(advTab, width=5)
bpm_entry.grid(column=7,row=1)

# For standard, add +/- buttons for BPM
bpm_plus_btn = Button(stdTab, text="+", width=3, command=increase_bpm)
bpm_plus_btn.grid(column=7, row=1)
bpm_minus_btn = Button(stdTab, text="-", width=3, command=decrease_bpm)
bpm_minus_btn.grid(column=8, row=1)

# Initialize Entry with default bpm = 75
bpm_entry.insert(0,str(default_bpm))

# Preset themes/chords for Basic/Standard
#-----------
theme_lbl = Label(stdTab, text="Theme:", font=("Arial",10))
theme_lbl.grid(column=6, row=3, sticky="W")

# Define list with keys
themeVar = StringVar(root)
themes = ['-Choose-','Cheerful','Somber']
themeVar.set(themes[0]) # set the default option

chooseThemeMenu = OptionMenu(stdTab, themeVar, *themes,command=update_theme)
chooseThemeMenu.grid(column=7, row=3, columnspan=3, sticky="W")

# Major key
#-----------
key_lbl = Label(advTab, text="Key:", font=("Arial",10))
key_lbl.grid(column=6, row=2, sticky="W")
# Define list with keys
keyVar = StringVar(root)
keys = ('C','D','E','F','G','A','B')
keyVar.set(keys[0]) # set the default option

choosekeyMenu = OptionMenu(advTab, keyVar, *keys,command=update_labels)
choosekeyMenu.grid(column=7, row=2, sticky="W")

#%% Define buttons for piano keys to play asynchronously over background chords
bkey_row = 3
wkey_row = 4

key_width = 5
key_height = 7

# C# key
Csharp_btn = Button(piano_frame, width=key_width, height=key_height, text="C#", command=music_dict('C#4').sound.play, bg="black", fg="white")
Csharp_btn.grid(column=1, columnspan=2,row=bkey_row)

# Dsharp key
Dsharp_btn = Button(piano_frame, width=key_width, height=key_height, text="D#", command=music_dict('D#4').sound.play, bg="black", fg="white")
Dsharp_btn.grid(column=3, columnspan=2,row=bkey_row)

# Fsharp key
Fsharp_btn = Button(piano_frame, width=key_width, height=key_height, text="F#", command=music_dict('F#4').sound.play, bg="black", fg="white")
Fsharp_btn.grid(column=7, columnspan=2,row=bkey_row)

# Gsharp key
Gsharp_btn = Button(piano_frame, width=key_width, height=key_height, text="G#", command=music_dict('G#4').sound.play, bg="black", fg="white")
Gsharp_btn.grid(column=9, columnspan=2,row=bkey_row)

# Asharp key
Asharp_btn = Button(piano_frame, width=key_width, height=key_height, text="A#", command=music_dict('A#4').sound.play, bg="black", fg="white")
Asharp_btn.grid(column=11, columnspan=2,row=bkey_row)

# C key
C_btn = Button(piano_frame, width=key_width, height=key_height, text="C", command=music_dict('C4').sound.play, bg="white", fg="black")
C_btn.grid(column=0, columnspan=2, row=wkey_row)

# D key
D_btn = Button(piano_frame, width=key_width, height=key_height, text="D", command=music_dict('D4').sound.play, bg="white", fg="black")
D_btn.grid(column=2, columnspan=2,row=wkey_row)

# E key
E_btn = Button(piano_frame, width=key_width, height=key_height, text="E", command=music_dict('E4').sound.play, bg="white", fg="black")
E_btn.grid(column=4, columnspan=2,row=wkey_row)

# F key
F_btn = Button(piano_frame, width=key_width, height=key_height, text="F", command=music_dict('F4').sound.play, bg="white", fg="black")
F_btn.grid(column=6, columnspan=2,row=wkey_row)

# G key
G_btn = Button(piano_frame, width=key_width, height=key_height, text="G", command=music_dict('G4').sound.play, bg="white", fg="black")
G_btn.grid(column=8, columnspan=2,row=wkey_row)

# A key
A_btn = Button(piano_frame, width=key_width, height=key_height, text="A", command=music_dict('A4').sound.play, bg="white", fg="black")
A_btn.grid(column=10, columnspan=2,row=wkey_row)

# B key
B_btn = Button(piano_frame, width=key_width, height=key_height, text="B", command=music_dict('B4').sound.play, bg="white", fg="black")
B_btn.grid(column=12, columnspan=2,row=wkey_row)

#%% Main menu at bottom

# Picture for create option in menu
create_icon_file = r".\icons\Menu_WriteIcon.png"
photo = PhotoImage(file = create_icon_file) 
# Resizing image to fit on button 
create_menu_img = photo.subsample(6) 

# Button to choose Create option
create_btn = Button(menu_frame, width=36,height=36, image=create_menu_img)
create_btn.grid(column=1,row=wkey_row+1, padx=18)

# Picture for listen option in menu
listen_icon_file = r".\icons\Menu_ListenIcon.png"
photo = PhotoImage(file = listen_icon_file) 
# Resizing image to fit on button 
listen_menu_img = photo.subsample(6) 

# Button to choose Listen option
listen_btn = Button(menu_frame, width=36,height=36, image=listen_menu_img)
listen_btn.grid(column=2, row=wkey_row+1, padx=18)

# Picture for profile option in menu
profile_icon_file = r".\icons\Menu_ProfileIcon.png"
photo = PhotoImage(file = profile_icon_file) 
# Resizing image to fit on button 
profile_menu_img = photo.subsample(6) 

# Button to choose profile option
profile_btn = Button(menu_frame, width=36,height=36, image=profile_menu_img)
profile_btn.grid(column=3, row=wkey_row+1, padx=18)

# Picture for setting option in menu
settings_icon_file = r".\icons\Menu_SettingsIcon.png"
photo = PhotoImage(file = settings_icon_file) 
# Resizing image to fit on button 
settings_menu_img = photo.subsample(6) 

# Button to choose setting option
settings_btn = Button(menu_frame, width=36,height=36, image=settings_menu_img)
settings_btn.grid(column=4, row=wkey_row+1, padx=18)

#%% Run GUI
root.mainloop()