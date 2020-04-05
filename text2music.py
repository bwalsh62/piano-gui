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

from piano_notes import music_theme
from gui_functions import mel_wav_write
from text_util import key_dict

# Music player from pygame
from pygame import mixer

#%% Input command

def text2music(input_command = 'Play a pop background in D'):
    
    #%% Interpret key words
    
    # BACKGROUND
    # -----
    # Define dictionary to translate key words into interpreted mode
    play_mode_dict = {
            "background":"chords_theme",
            "chord":"single_chord",
            "beat":"with_beat"}
    play_mode_dict_list = list(play_mode_dict.keys())
    
    # Define default mode
    default_mode = play_mode_dict_list[0]
    
    # Dictionary to set equivalence of words for theme
    theme_dict = {
            "cheerful":"cheerful",
            "happy":"cheerful",
            "sad":"somber",
            "somber":"somber",
            "pop":"pop",
            "mainstream":"pop"}
    
    theme_dict_list = list(theme_dict.keys())
    # Define default theme
    default_theme = theme_dict_list[0]
    
    # Find matching modes
    found_modes = [mode_idx for mode_idx,key in enumerate(play_mode_dict_list) if input_command.find(key)>-1]
    
    # Give warning and default / give example if no mode found
    if len(found_modes)==0:
        chosen_mode = default_mode
        print('No modes recognized. Defaulting to {} mode'.format(default_mode))
    elif len(found_modes)>1:
        chosen_modes = [play_mode_dict_list[mode] for mode in found_modes]
        for idx,mode in enumerate(chosen_modes):
            print('Interpreted mode {}: {}'.format(idx+1,mode))
    else:
        chosen_mode = play_mode_dict_list[found_modes[0]]
        print('Interpreted mode: {}'.format(chosen_mode))
    
    # N_LOOP
    # ----- 
    # Define dictionary to translate key words into interpreted # times to loop
    n_loop_dict = {
            "one time":1,
            "once":1,
            "two times":2,
            "twice":2,
            "three times":3,
            "four times":4,
            "five times":5,
            "ten times":10,
            "for a while":100}
    
    n_loop_dict_list = list(n_loop_dict.keys())
    # Define default theme
    default_n_loop = n_loop_dict_list[0]
    
    # KEY
    # ----- 
    
    key_dict_list = list(key_dict.keys())
    # Define default theme
    default_key = key_dict_list[0]
    
    #%% Should have an integrated class that looks for specific features of each play mode
        
    # Look for n_loops 
    found_loop_keys = [key for loop_idx,key in enumerate(n_loop_dict) if input_command.find(key)>-1]
    # Give warning and default / give example if no mode found
    if len(found_loop_keys)==0:
        chosen_n_repeats = n_loop_dict[default_n_loop]
        print('No number of loops recognized. Defaulting to {}'.format(default_n_loop))
    else:
        chosen_n_repeats = n_loop_dict[found_loop_keys[0]]
        print('Interpreted number of loops: {}'.format(chosen_n_repeats))
    
    # Generalize for multiple modes found

    if len(found_modes)>1:
        hip_hop_beat_bpm_128 = r"C:\Users\benja\Music\Cymatics-HipHopStarterPack\Drums-Loops\Loops-Full\Hip-HopDrumLoop1-128BPM.wav"

        hip_hop_beat_bpm_100 = r"C:\Users\benja\Music\Cymatics-HipHopStarterPack\Drums-Loops\Loops-Full\Hip-HopDrumLoop1-100BPM.wav"
        
        hip_hop_theme_mel_bpm_128 = r"C:\Users\benja\Music\Cymatics-HipHopStarterPack\MelodyLoops\Hip-HopMelodyLoop2-128BPMEMin.wav"
        
        hip_hop_theme_mel_bpm_100 = r"C:\Users\benja\Music\Cymatics-HipHopStarterPack\MelodyLoops\Hip-HopMelodyLoop2-100BPMEMin.wav"
        
        bpm = 100
#        time_intro = 16/bpm*60

        # Play music
        
        if bpm == 100:
            hip_hop_beat = hip_hop_beat_bpm_100
            hip_hop_theme_mel = hip_hop_theme_mel_bpm_100
        elif bpm == 128:
            hip_hop_beat = hip_hop_beat_bpm_128
            hip_hop_theme_mel = hip_hop_theme_mel_bpm_128
        
        beat = mixer.Sound(hip_hop_beat)
        
        theme_mel = mixer.Sound(hip_hop_theme_mel)
        
#        theme_mel.play(loops=0)
#        # Pause for intro
#        time.sleep(time_intro)
        
        beat.play(loops=chosen_n_repeats-1) 
        theme_mel.play(loops=chosen_n_repeats-1)
    else:
    
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
            
            # Look for key (if a background mode? should be agnostic)
            found_keys = [key for idx,key in enumerate(key_dict) if input_command.find(key)>-1]
            # Give warning and default / give example if no mode found
            if len(found_keys)==0:
                chosen_key = key_dict[default_key]
                print('No keys recognized. Defaulting to {}'.format(default_key))
            else:
                chosen_key = key_dict[found_keys[0]]
                print('Interpreted key: {}'.format(chosen_key))
        
    #%% Play music based on function
    
    if len(found_modes)>1:
        print("")
    else:
    
        if chosen_mode == 'background':
            
            # from play_music_func - should be shared
            chords_full = ('C','C#','D','D#','E','F','F#','G','G#','A','A#','B')
            key_const = chords_full.index(chosen_key) # chosen_key = 'D' -> keyConst = 2
                    
            mel1_wav, mel2_wav, mel3_wav, hum_mel_wav = mel_wav_write(bpm=theme_chords_obj.bpm, 
                            base_note_arr = theme_chords_obj.chords, 
                            key_constant=key_const)
            
            melody1 = mixer.Sound(mel1_wav)
            melody2 = mixer.Sound(mel2_wav)
            melody3 = mixer.Sound(mel3_wav)
        
            melody1.play(loops=chosen_n_repeats-1)
            melody2.play(loops=chosen_n_repeats-1)
            melody3.play(loops=chosen_n_repeats-1)
    
    #%% Prototype as a class
    
    # TEST for class eventually
    #------------------------
    # play_music_obj.play()