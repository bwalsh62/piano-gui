# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 20:56:26 2019

@author: benja

Music from: http://theremin.music.uiowa.edu/MISpiano.html

# TO DO
# - Try as a class

"""
from pygame import mixer
#from os import getcwd

mixer.init()

# Paths to piano wav files
music_fpath = "./music_files/piano/"
C_path = music_fpath+"Piano.mf.C4_2p4s.wav"
Csharp_path = music_fpath+"Piano.mf.Db4_2p5s.wav"
D_path = music_fpath+"Piano.mf.D4_2p4s.wav"
Dsharp_path = music_fpath+"Piano.mf.Eb4_2p5s.wav"
E_path = music_fpath+"Piano.mf.E4_2p4s.wav"
F_path = music_fpath+"Piano.mf.F4_2p4s.wav"
Fsharp_path = music_fpath+"Piano.mf.Gb4_2p5s.wav"
G_path = music_fpath+"Piano.mf.G4_2p4s.wav"
Gsharp_path = music_fpath+"Piano.mf.Ab4_2p5s.wav"
A_path = music_fpath+"Piano.mf.A4_2p4s.wav"
Asharp_path = music_fpath+"Piano.mf.Bb4_2p5s.wav"
B_path = music_fpath+"Piano.mf.B4_2p4s.wav"

# Define sounds
sound_C = mixer.Sound(C_path)
sound_Csharp = mixer.Sound(Csharp_path)
sound_D = mixer.Sound(D_path)
sound_Dsharp = mixer.Sound(Dsharp_path)
sound_E = mixer.Sound(E_path)
sound_F = mixer.Sound(F_path)
sound_Fsharp = mixer.Sound(Fsharp_path)
sound_G = mixer.Sound(G_path)
sound_Gsharp = mixer.Sound(Gsharp_path)
sound_A = mixer.Sound(A_path)
sound_Asharp = mixer.Sound(Asharp_path)
sound_B = mixer.Sound(B_path)

sound_dict = {
        'C4': sound_C,
        'C#4': sound_Csharp,
        'D4': sound_D,
        'D#4': sound_Dsharp,
        'E4': sound_E,
        'F4': sound_F,
        'F#4': sound_Fsharp,
        'G4': sound_G,
        'G#4': sound_Gsharp,
        'A4': sound_A,
        'A#4': sound_Asharp,
        'B4': sound_B,
}

sound_path_dict = {
        'C4': C_path,
        'C#4': Csharp_path,
        'D4': D_path,
        'D#4': Dsharp_path,
        'E4': E_path,
        'F4': F_path,
        'F#4': Fsharp_path,
        'G4': G_path,
        'G#4': Gsharp_path,
        'A4': A_path,
        'A#4': Asharp_path,
        'B4': B_path,
}

note_indices = ('C4','C#4','D4','D#4','E4',\
        'F4','F#4','G4','G#4','A4','A#4','B4')

sound_paths = [C_path, Csharp_path, D_path, Dsharp_path,\
               E_path, F_path, Fsharp_path, G_path, Gsharp_path, \
A_path, Asharp_path, B_path]

#%%    
freq_dict = {
        'D2': 73.42,
        'E2': 82.41,
        'F2': 87.31,
        'G2': 98.00,
        'A2': 110.00,
        'B2': 123.47,
        'C3': 130.81,
        'D3': 146.83,
        'E3': 164.81,
        'F3': 174.61,
        'G3': 196.00,
        'A3': 220.00,
        'B3': 246.94,
        'C4': 261.63,
        'C#4': 277.187,
        'D4': 293.66,
        'D#4': 311.13,
        'E4': 329.63,
        'F4': 349.23,
        'F#4': 370.00,
        'G4': 392.00,
        'G#4': 415.312,
        'A4': 440.00,
        'A#4': 466.172,
        'B4': 493.88,
        'C5': 523.25,
        'D5': 587.33,
        'E5': 659.25,
        'F5': 698.46,
        'G5': 783.99
}

#%% Music dictionary

class music_dict:
        
    def __init__(self, note):        
        
        default_note = 'C4'
        
        if note in sound_dict.keys():
            self.note = note # frequency in Hz
            self.freq = freq_dict[note]
            self.sound = sound_dict[note] 
        else:                
            print('Unknown input {}, setting to {}'.format(note,default_note))
            self.note = default_note
            self.freq = freq_dict[note]
            self.sound = sound_dict[note]

#%%
class music_theme:
    def __init__(self, theme='pop'):        
        self.theme = theme.lower() 
        default_theme = 'pop'
        
        if self.theme == 'somber':
            self.chords = [5,1,2,5]
            self.bpm = 55
        elif self.theme == 'cheerful':
            self.chords = [0,3,4,0]
            self.bpm = 75
        elif self.theme == 'pop':
            self.chords = [0,4,5,3]
            self.bpm = 70
        else:
            print('Unknown input theme {}\nSetting to default {}'.format(self.theme,default_theme)) 
            self.theme = default_theme
            self.chords = [0,4,5,3]
            self.bpm = 70