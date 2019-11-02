# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 11:11:36 2019

Last updated: November 2, 2019

@author: Ben Walsh
for liloquy

----------------------------------------

Called by piano_chord_gui to make melody wav files from GUI slider values

Example: 
melody_wav = make_melody('./outputmelody.wav',1,4,5,1)
# Makes a melody of C-F-G-C notes

----------------------------------------
# TO DO
- Fix why note_repeats=2 repeats to 4
--  Doubling the note lengths, 1-2-4 etc. not actually repeating
- To fix above, can update wav_file_clip to have optional arg for name/suffix
   then initialize a separate note_array for repeated notes

"""

#%% Import custom libraries
from piano_notes import C_path, D_path, E_path, F_path, G_path, A_path, B_path
# Custom wav_file helper functions
from wav_utils import wav_file_append, wav_file_clip

sound_paths = [C_path,D_path,E_path,F_path,G_path,A_path,B_path]

#%% Make melody wav file from input notes

def make_melody(mel_wav_name,note_array,bpm=60):
    
    t_len = 60/bpm # time in seconds
    note_repeats = 2 # assume 2 for now, can be input or based on bpm and 4/4
    
    for idx, note_num, in enumerate(note_array):
        # Path of corresponding wav file
        note_wav_file = sound_paths[note_num]
        # Generate wav file and return new name
        note_wav_file = wav_file_clip(t_len,note_wav_file)
        # If notes are repeated, append to existing wav file
        # Below keeps doubling the note lengths, 1-2-4 etc. not actually repeating
        for repeat in range(1):
            wav_file_append(note_wav_file,note_wav_file,note_wav_file)
        if idx==0:
            # Initalize melody name
            mel_wav_name = wav_file_clip(t_len*note_repeats,note_wav_file)
        elif idx>0:
            wav_file_append(mel_wav_name,note_wav_file,mel_wav_name)
        
    return mel_wav_name