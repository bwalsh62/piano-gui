# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 20:30:43 2020

@author: Ben Walsh
for liloquy

"""

# Play a happy/cheerful background

# Play a sad/somber background

# Play a 1-5-6-4 chord progression in the key of C

# Play C F G C chords

# Play a C chord

#%% Import libraries

from piano_notes import music_theme
from gui_functions import play_music_func

#%% Input command

input_command_single = "Play a C chord"
input_command_background = "Play a sad background"
input_command_unrecog = "Play whatever"

input_command = input_command_background

print("Input command ...\n{}".format(input_command))

#%% Interpret key words

# Define dictionary to translate key words into interpreted mode
play_mode_dict = {
        "background":"chords_theme",
        "chord":"single_chord"}
play_mode_dict_list = list(play_mode_dict.keys())

# Define default mode
default_mode = play_mode_dict_list[0]

# Dictionary to set equivalence of words
theme_dict = {
        "cheerful":"cheerful",
        "happy":"cheerful",
        "sad":"somber",
        "somber":"somber"}

theme_dict_list = list(theme_dict.keys())
# Define default theme
default_theme = theme_dict_list[0]

# Find matching modes
found_modes = [mode_idx for mode_idx,key in enumerate(play_mode_dict_list) if input_command.find(key)>-1]

# Give warning and default / give example if no mode found
if len(found_modes)==0:
    chosen_mode = default_mode
    print('No modes recognized. Defaulting to {} mode'.format(default_mode))
else:
    chosen_mode = play_mode_dict_list[found_modes[0]]
    print('Interpreted mode: {}'.format(chosen_mode))

#%% Should have an integrated class that looks for specific features of each play mode

if chosen_mode == 'background':
    # Look for theme if a background mode
    
    found_themes = [theme_idx for theme_idx,key in enumerate(theme_dict_list) if input_command.find(key)>-1]
    # Give warning and default / give example if no mode found
    if len(found_themes)==0:
        chosen_theme = default_theme
        print('No themes recognized. Defaulting to {}'.format(default_theme))
    else:
        chosen_theme = theme_dict_list[found_themes[0]]
        print('Interpreted theme: {}'.format(chosen_theme))
    
    theme_chords_obj = music_theme(theme_dict[chosen_theme])

#%% Play music based on function

if chosen_mode == 'background':
    play_music_func(bpm=theme_chords_obj.bpm, base_note_arr = theme_chords_obj.chords, n_repeats=1)

#%% Prototype as a class

# TEST for class eventually
#------------------------
# play_music_obj.play()