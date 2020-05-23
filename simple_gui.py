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

from gui_functions import mel_wav_write
#from melody import mel_wav_write
#from wav_util import wav_write_melody

#%% Define constants

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 500
MENU_HEIGHT = 100

MENU_CONFIG = 'config.yaml'

#%% Initialize GUI

main = Tk()
main.title('liloquy - find your song')
main.geometry('{}x{}'.format(300, SCREEN_HEIGHT))

# Create main frame containers

main_frame = Frame(main, bg='brown', width=SCREEN_WIDTH, height=SCREEN_HEIGHT-MENU_HEIGHT, pady=166, padx=116)
menu_frame = Frame(main, bg='gray', width=SCREEN_WIDTH, height=MENU_HEIGHT, padx=2, pady=2)

# layout main containers
main.grid_rowconfigure(1, weight=1)
main.grid_columnconfigure(0, weight=1)

main_frame.grid(row=0)
menu_frame.grid(row=1, sticky="ew")

#%% Play_music_lite - eventually import

def play_music_lite(bpm=64, chords=[0 ,0, 4, 4, 5, 5, 3, 3], n_plays=1):

    mel1_wav, mel2_wav, mel3_wav, hum_mel_wav = mel_wav_write(bpm, chords)
    
    melody1 = mixer.Sound(mel1_wav)
    melody2 = mixer.Sound(mel2_wav)
    melody3 = mixer.Sound(mel3_wav)
    
    melody1.play(loops=n_plays-1)
    melody2.play(loops=n_plays-1)
    melody3.play(loops=n_plays-1)

#%% Play button

with open(MENU_CONFIG) as file:
    btn_cfg = yaml.load(file, Loader=yaml.FullLoader)

# Picture for play button
play_img_file = btn_cfg['play']['img_file']
if not(os.path.exists(play_img_file)):
    print(f'Cannot find: {play_img_file}')
    
photo = PhotoImage(file=play_img_file)
 
# Resizing image to fit on button 
play_img = photo.subsample(4) 

play_music_btn = Button(main_frame, \
                        width=btn_cfg['play']['width'], \
                        height=btn_cfg['play']['height'], \
                        text="Play", image=play_img, command=play_music_lite)

play_music_btn.grid(column=btn_cfg['play']['grid_col'], \
                    row=btn_cfg['play']['grid_row'])

#%% Run GUI

main.mainloop()