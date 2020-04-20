# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 12:32:36 2019

Last updated: November 19, 2019

Called by piano_chord_gui.py

- Add function descriptions and usage of play_music_func

play_music_func(bpm, base_note_arr, n_repeats=1, key_constant=0, play_chords_sel=1, play_mel_sel=0)

bpm :           beats per minute   bpm=70
base_note_arr:  base note array    base_note_arr = [0,4,5,3]
etc...
    
@author: Ben Walsh
for liloquy
"""
#%% Import libraries
# Custom music function for making melody
from melody import make_melody

#%% Define function

# 
# Callback when pressing Play on GUI
#

def mel_wav_write(bpm, base_note_arr, key_constant=0):
    
    # Convert from 0=C, 1=D, 2=E, 3=F... to 0=C, 2=D, 4=E, 5=F, ...
    note_chord_map = [0,2,4,5,7,9,11]
    note_array = [(note_chord_map[note]+key_constant)%12 for note in base_note_arr]
    
    # For a minor chord, 3rd note is flat
    # Example in key of C, Dm has F, not F#
    flat_third = [(note==1 or note==2 or note==5) for note in base_note_arr]
    
    # Top-line melody
    mel1_wav_name = './mel1.wav'
    mel1_wav_name = make_melody(mel1_wav_name,note_array,bpm,debug=0)

    mel2_wav_name = './mel2.wav'
    mel2_wav_name = make_melody(mel2_wav_name,[(note+4-flat_third[idx])%12 for idx,note in enumerate(note_array)],bpm)

    mel3_wav_name = './mel3.wav'
    mel3_wav_name = make_melody(mel3_wav_name,[(idx+7)%12 for idx in note_array],bpm)

    # Should be input argument or defined from common location
    hum_mel_wav_name = './mel_hum.wav'

    return mel1_wav_name, mel2_wav_name, mel3_wav_name, hum_mel_wav_name

#%% Visualize timer and sleep while recording

import time

def record_timer_viz(note_len_time=1,rec_notes_total=1):
    
    start_time = time.time()
    
    ticks_per_note = 4
    
    n_counter = ticks_per_note*rec_notes_total
    for counter in range(n_counter):
        for idx1 in range(counter):
            if idx1 % ticks_per_note == 0:
                print('|',end='')
            print('*',end='')
        for idx2 in range(n_counter-counter):
            if (counter+idx2) % ticks_per_note == 0:
                print('|',end='')
            print('-',end='')
        time.sleep(note_len_time/ticks_per_note)
        print('\n',end='')
    
    elapsed_time = time.time() - start_time

    return elapsed_time

#%% Record sound and point to timer visualization

import sounddevice as sd

def record_music(rec_notes_total, note_len_time, fs=44.1e3):
    
    # Samples in a note = the samples/second * time   
    note_len_n_samples = int(fs * note_len_time)
    
    # Record for data points = number of notes * data points / note
    recorded_sound = sd.rec(rec_notes_total*note_len_n_samples, samplerate=fs, channels=2)
    
    # Visualize timer while recording
    record_timer_viz(note_len_time,rec_notes_total)

    return recorded_sound
