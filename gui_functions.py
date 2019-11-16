# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 12:32:36 2019

Called by piano_chord_gui.py

@author: Ben Walsh
for liloquy
"""
#%% Import libraries
# Custom music function for making melody
from melody import make_melody

# Music player from pygame
from pygame import mixer

#%% Define function
def chords_repeat_func(bpm, n_repeats, base_notes_array):
    
    # Top-line melody
    mel1_wav_name = './mel1.wav'
    mel1_wav_name = make_melody(mel1_wav_name,base_notes_array,bpm)

    mel2_wav_name = './mel2.wav'
    mel2_wav_name = make_melody(mel2_wav_name,(base_notes_array+2)%7,bpm)

    mel3_wav_name = './mel3.wav'
    mel3_wav_name = make_melody(mel3_wav_name,(base_notes_array+4)%7,bpm)

    melody1 = mixer.Sound(mel1_wav_name)
    melody2 = mixer.Sound(mel2_wav_name)
    melody3 = mixer.Sound(mel3_wav_name)

    melody1.play(loops=n_repeats)
    melody2.play(loops=n_repeats)
    melody3.play(loops=n_repeats)
