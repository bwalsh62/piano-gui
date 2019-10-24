# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 11:11:36 2019

Last updated: October 24, 2019

@author: Ben Walsh
for liloquy

----------------------------------------

Called by piano_chord_gui to make melody wav files from GUI slider values
Currently hard-coded to 4-note melodies

Example: 
melody_wav = make_melody('./outputmelody.wav',1,4,5,1)
# Makes a melody of C-F-G-C notes

----------------------------------------
# TO DO
- Generalize to any length melody, not hard-coded to 4
- Investigate why note_repeats=2 repeats to 4?

"""

#%% Import custom libraries
from piano_notes import C_path, D_path, E_path, F_path, G_path, A_path, B_path
# Custom wav_file helper functions
from wav_utils import wav_file_append, wav_file_clip

sound_paths = [C_path,D_path,E_path,F_path,G_path,A_path,B_path]

#%% Make melody wav file from input notes

def make_melody(mel_wav_name,note_num1,note_num2,note_num3,note_num4,bpm=60):
    
    # Assuming 4 beats per measure and quarter notes
    t_len = 60/bpm # time in seconds
    note_repeats = 2 # assume 2 for now, can be input or based on bpm and 4/4
    
    wav_file1 = sound_paths[note_num1] # or eventually sounds[note_num1].path
    wav_file1 = wav_file_clip(t_len,wav_file1)
    for repeat in range(note_repeats):
        wav_file_append(wav_file1,wav_file1,wav_file1)
    wav_file2 = sound_paths[note_num2] # or eventually sounds[note_num2].path
    wav_file2 = wav_file_clip(t_len,wav_file2)
    for repeat in range(note_repeats):
        wav_file_append(wav_file2,wav_file2,wav_file2)
    wav_file_append(wav_file1,wav_file2,mel_wav_name)
    wav_file3 = sound_paths[note_num3] # or eventually sounds[note_num2].path
    wav_file3 = wav_file_clip(t_len,wav_file3)
    for repeat in range(note_repeats):
        wav_file_append(wav_file3,wav_file3,wav_file3)
    wav_file_append(mel_wav_name,wav_file3,mel_wav_name)
    wav_file4 = sound_paths[note_num4] # or eventually sounds[note_num2].path
    wav_file4 = wav_file_clip(t_len,wav_file4)
    for repeat in range(note_repeats):
        wav_file_append(wav_file4,wav_file4,wav_file4)
    wav_file_append(mel_wav_name,wav_file4,mel_wav_name)
        
    return mel_wav_name