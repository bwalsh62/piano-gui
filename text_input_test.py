# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 20:30:43 2020

@author: Ben Walsh
for liloquy

"""

# Play a 1-5-6-4 chord progression in the key of C

# Play C F G C chords

# Play a C chord

#%% Import libraries

#from piano_notes import music_theme
#from gui_functions import mel_wav_write
#from text_util import key_dict
#
## Music player from pygame
#from pygame import mixer

from text2music import text2music

#%% Input command

user_input_on = False

input_command_single = "Play a C chord"
input_cmd_background = "Play a pop background"
input_command_unrecog = "Play whatever"
input_cmd_with_percussion = "Play a background in E minor with a beat once" # At 100 BPM

if user_input_on:
    input_command = input('Input music command: ')
else:
    input_command = input_cmd_with_percussion

print("Input command ...\n{}".format(input_command))

#%%

text2music(input_command)
