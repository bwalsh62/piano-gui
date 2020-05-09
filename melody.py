# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 11:11:36 2019

Last updated: November 19, 2019

@author: Ben Walsh
for liloquy

----------------------------------------

Called by gui_functions to make melody wav files from GUI slider values

Example: 
melody_wav = make_melody('./outputmelody.wav',0,5,7,0)
# Makes a melody of C-F-G-C notes

----------------------------------------
# TO DO
- Fix why note_repeats=2 repeats to 4
--  Doubling the note lengths, 1-2-4 etc. not actually repeating

"""

#%% Import custom libraries
from piano_notes import sound_paths, sound_path_dict

# Custom wav_file helper functions
from wav_utils import wav_file_append, wav_file_clip

#%% Make melody wav file from input notes

def make_melody(mel_wav_name,note_array,bpm=60,mode="note_idx",vol_const=1,note_repeats=1,debug=0):
        
    t_len = 60/bpm # time in seconds
    
    if debug:
        print('Make melody, mode={}'.format(mode))
        print('note_array={}'.format(note_array))
        print('mel_wav_name={}'.format(mel_wav_name))
    
    # Allow inputs of 'C4' 'D4' etc.
    #---------------------------
    if mode=="note_name":
        for idx, note in enumerate(note_array):
            # Get note .wav file path
            note_wav_file = sound_path_dict[note]
            # Return new file path of _clipped .wav file
            note_wav_file = wav_file_clip(t_len,note_wav_file)
            if debug:
                print('note_wav_file = {}'.format(note_wav_file))
                print('idx = {}'.format(idx))
                print('note = {}'.format(note))

            # If notes are repeated, append to existing wav file
            # Below keeps doubling the note lengths, 1-2-4 etc. not actually repeating
            for repeat in range(1):
                # Repeat note
                # This should be to a new note, not overwriting the same note 
                wav_file_append(note_wav_file, note_wav_file, note_wav_file)
            if idx==0:
                # Initalize melody name
                mel_wav_name = wav_file_clip(t_len, note_wav_file, mel_wav_name)

            elif idx>0:
                wav_file_append(mel_wav_name,note_wav_file,mel_wav_name)
    elif mode=="note_idx": 
        for idx, note_num, in enumerate(note_array):
            # Path of corresponding wav file
            note_wav_file = sound_paths[note_num]
            # Generate wav file and return new name
            note_wav_file = wav_file_clip(t_len,note_wav_file)
            if debug:
                print('note_wav_file = {}'.format(note_wav_file))
                print('idx = {}'.format(idx))
                print('note_num = {}'.format(note_num))
                
            # If notes are repeated, append to existing wav file
            # Below keeps doubling the note lengths, 1-2-4 etc. not actually repeating
            for repeat in range(1):
                wav_file_append(note_wav_file,note_wav_file,note_wav_file)
            if idx==0:
                # Initalize melody name
                mel_wav_name = wav_file_clip(t_len,note_wav_file,mel_wav_name)
            elif idx>0:
                new_note_wav_name = './note{}.wav'.format(idx+1)
                new_note_wav_file = wav_file_clip(t_len, note_wav_file, new_note_wav_name)
                wav_file_append(mel_wav_name, new_note_wav_file, mel_wav_name)
    else:
        print("Mode {} for melody.py not recognized".format(mode))
    
    return mel_wav_name