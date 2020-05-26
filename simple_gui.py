# -*- coding: utf-8 -*-
"""

Updated GUI with simpler interface

Created on Sat May 23 09:54:29 2020

@author: Ben Walsh
for liloquy
Copyright 2020 Benjamin Walsh

"""

#%% Import libraries

from tkinter import Tk, Label, Button, Scale, Frame, Entry, PhotoImage, ttk, OptionMenu, Checkbutton, StringVar, IntVar
import os
import yaml
from pygame import mixer

from gui_functions import mel_wav_write2
# Should be...
#from melody import mel_wav_write
#from wav_util import wav_write_melody
# Or could be...
# from music_functions import play_music_lite

#%% Define constants

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 500
MENU_HEIGHT = 100

MENU_CONFIG_FILE = 'menu_config.yaml'

with open(MENU_CONFIG_FILE) as file:
    menu_cfg = yaml.load(file, Loader=yaml.FullLoader)

#%% Initialize GUI

main = Tk()
main.title('liloquy - find your song')
main.geometry('{}x{}'.format(300, menu_cfg['screen_height']))

# Create main frame containers

main_frame = Frame(main, bg='brown', width=menu_cfg['screen_width'], height=menu_cfg['screen_height']-MENU_HEIGHT, pady=30, padx=18)
menu_frame = Frame(main, bg='gray', width=menu_cfg['screen_width'], height=menu_cfg['menu_height'], padx=2, pady=2)

# layout main containers
main.grid_rowconfigure(1, weight=1)
main.grid_columnconfigure(0, weight=1)

main_frame.grid(row=0)
menu_frame.grid(row=1, sticky="ew")

#%% Play_music_lite - eventually import?

def play_music_lite(bpm=64, chords=[0, 0, 4, 4, 5, 5, 3, 3], n_plays=1, chord_len=3):

    # Eventually reference in modular location
    hip_hop_beat = r"C:\Users\benja\Music\Cymatics-HipHopStarterPack\Drums-Loops\Loops-Full\Hip-HopDrumLoop1-128BPM.wav"
    beats = mixer.Sound(hip_hop_beat)
    
    melody_wav_files = mel_wav_write2(bpm, chords, chord_len=3)
    
    for melody in melody_wav_files:
        mixer.Sound(melody).play(loops=n_plays-1)
        
    if beats_on.get():
        beats.play(loops=n_plays-1)
        
#%% Toggle beats_on - eventually import?

# Define list with music mixing options
beats_on = IntVar(main, name="beats_on")
main.setvar(name="beats_on", value = 0)

def toggle_beats_on():
    main.setvar(name="beats_on", value=not(beats_on.get()))

#%% Music mixer

# Picture for mixer
mix_img_file = menu_cfg['mixer']['img_file']
if not(os.path.exists(mix_img_file)):
    print(f'Cannot find: {mix_img_file}')
 
# Resizing image to fit on button 
mixer_img = PhotoImage(file=mix_img_file).subsample(4) 

mixer_btn = Button(main_frame, \
                        width=menu_cfg['mixer']['width'], \
                        height=menu_cfg['mixer']['height'], \
                        text="Play", image=mixer_img, command=play_music_lite)

mixer_btn.grid(column=menu_cfg['mixer']['grid_col'], \
                    row=menu_cfg['mixer']['grid_row'], pady=10)

#%% Drums button

# Picture for drums
drums_img_file = menu_cfg['drums']['img_file']
if not(os.path.exists(drums_img_file)):
    print(f'Cannot find: {drums_img_file}')
 
# Resizing image to fit on button 
drums_img = PhotoImage(file=drums_img_file).subsample(2) 

drums_btn = Button(main_frame, \
                        width=menu_cfg['drums']['width'], \
                        height=menu_cfg['drums']['height'], \
                        text="Play", image=drums_img, command=toggle_beats_on)

drums_btn.grid(column=menu_cfg['drums']['grid_col'], \
                    row=menu_cfg['drums']['grid_row'], pady=4)

#%% Play button

# Picture for play button
play_img_file = menu_cfg['play']['img_file']
if not(os.path.exists(play_img_file)):
    print(f'Cannot find: {play_img_file}')
     
# Resizing image to fit on button 
play_img = PhotoImage(file=play_img_file).subsample(4) 

play_music_btn = Button(main_frame, \
                        width=menu_cfg['play']['width'], \
                        height=menu_cfg['play']['height'], \
                        text="Play", image=play_img, command=play_music_lite)

play_music_btn.grid(column=menu_cfg['play']['grid_col'], \
                    row=menu_cfg['play']['grid_row'], pady=30)

#%% Run GUI

main.mainloop()