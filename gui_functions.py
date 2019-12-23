# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 12:32:36 2019

Last updated: November 19, 2019

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
def chords_repeat_func(bpm, n_repeats, base_notes_array, key_constant=0):
    
    # Convert from 0=C, 1=D, 2=E, 3=F... to 0=C, 2=D, 4=E, 5=F, ...
    note_chord_map = [0,2,4,5,7,9,11]
    note_array = [(note_chord_map[note]+key_constant)%12 for note in base_notes_array]
    
    # For a minor chord, 3rd note is flat
    # Example in key of C, Dm has F, not F#
    flat_third = [(note==1 or note==2 or note==5) for note in base_notes_array]
    
    # Top-line melody
    mel1_wav_name = './mel1.wav'
    mel1_wav_name = make_melody(mel1_wav_name,note_array,bpm,debug=0)

    mel2_wav_name = './mel2.wav'
    mel2_wav_name = make_melody(mel2_wav_name,[(note+4-flat_third[idx])%12 for idx,note in enumerate(note_array)],bpm)

    mel3_wav_name = './mel3.wav'
    mel3_wav_name = make_melody(mel3_wav_name,[(idx+7)%12 for idx in note_array],bpm)

    melody1 = mixer.Sound(mel1_wav_name)
    melody2 = mixer.Sound(mel2_wav_name)
    melody3 = mixer.Sound(mel3_wav_name)

    melody1.play(loops=n_repeats)
    melody2.play(loops=n_repeats)
    melody3.play(loops=n_repeats)
