# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 20:56:26 2019

@author: Ben Walsh

For Elly

Copyright 2020

Music from: http://theremin.music.uiowa.edu/MISpiano.html

"""

#%% Import pygame library

from pygame import mixer

mixer.init()

#%% Paths to piano wav files

music_fpath = "./music_files/piano/"
C3_path = f"{music_fpath}Piano.mf.C3_3s.wav"
D3_path = music_fpath+"Piano.mf.D3_3s.wav"
E3_path = music_fpath+"Piano.mf.E3_3s.wav"
F3_path = music_fpath+"Piano.mf.F3_3s.wav"
G3_path = music_fpath+"Piano.mf.G3_3s.wav"
A3_path = music_fpath+"Piano.mf.A3_3s.wav"
B3_path = music_fpath+"Piano.mf.B3_3s.wav"

C4_path = music_fpath+"Piano.mf.C4_2p4s.wav"
Csharp_path = music_fpath+"Piano.mf.Db4_2p5s.wav"
D4_path = music_fpath+"Piano.mf.D4_2p4s.wav"
Dsharp_path = music_fpath+"Piano.mf.Eb4_2p5s.wav"
E4_path = music_fpath+"Piano.mf.E4_2p4s.wav"
F4_path = music_fpath+"Piano.mf.F4_2p4s.wav"
Fsharp_path = music_fpath+"Piano.mf.Gb4_2p5s.wav"
G4_path = music_fpath+"Piano.mf.G4_2p4s.wav"
Gsharp_path = music_fpath+"Piano.mf.Ab4_2p5s.wav"
A4_path = music_fpath+"Piano.mf.A4_2p4s.wav"
Asharp_path = music_fpath+"Piano.mf.Bb4_2p5s.wav"
B4_path = music_fpath+"Piano.mf.B4_2p4s.wav"

# Define sounds
sound_C3 = mixer.Sound(C3_path)
sound_D3 = mixer.Sound(D3_path)
sound_E3 = mixer.Sound(E3_path)
sound_F3 = mixer.Sound(F3_path)
sound_G3 = mixer.Sound(G3_path)
sound_A3 = mixer.Sound(A3_path)
sound_B3 = mixer.Sound(B3_path)

sound_C4 = mixer.Sound(C4_path)
sound_Csharp = mixer.Sound(Csharp_path)
sound_D4 = mixer.Sound(D4_path)
sound_Dsharp = mixer.Sound(Dsharp_path)
sound_E4 = mixer.Sound(E4_path)
sound_F4 = mixer.Sound(F4_path)
sound_Fsharp = mixer.Sound(Fsharp_path)
sound_G4 = mixer.Sound(G4_path)
sound_Gsharp = mixer.Sound(Gsharp_path)
sound_A = mixer.Sound(A4_path)
sound_Asharp = mixer.Sound(Asharp_path)
sound_B4 = mixer.Sound(B4_path)

sound_dict = {
        'C3': sound_C3,
        'D3': sound_D3,
        'E3': sound_E3,
        'F3': sound_F3,
        'G3': sound_G3,
        'A3': sound_A3,
        'B3': sound_B3,
        'C4': sound_C4,
        'C#4': sound_Csharp,
        'D4': sound_D4,
        'D#4': sound_Dsharp,
        'E4': sound_E4,
        'F4': sound_F4,
        'F#4': sound_Fsharp,
        'G4': sound_G4,
        'G#4': sound_Gsharp,
        'A4': sound_A,
        'A#4': sound_Asharp,
        'B4': sound_B4,
}

sound_path_dict = {
        'C3': C3_path,
        'D3': D3_path,
        'E3': E3_path,
        'F3': F3_path,
        'G3': G3_path,
        'A3': A3_path,
        'C4': C4_path,
        'C#4': Csharp_path,
        'D4': D4_path,
        'D#4': Dsharp_path,
        'E4': E4_path,
        'F4': F4_path,
        'F#4': Fsharp_path,
        'G4': G4_path,
        'G#4': Gsharp_path,
        'A4': A4_path,
        'A#4': Asharp_path,
        'B4': B4_path,
}

note_indices = ('C4','C#4','D4','D#4','E4',\
        'F4','F#4','G4','G#4','A4','A#4','B4')


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
        'F#3': 185.00,
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

#%%    
scale = ('C3', 'C#3', 'D3', 'D#3', 'E3', \
              'F3', 'F#3', 'G3', 'G#3', 'A3', \
              'B3', 'C4', 'C#4', 'D4', 'D#4', \
              'E4', 'F4', 'F#4', 'G4', 'G#4', \
              'A4', 'A#4', 'B4')

#%% Melody dictionary

class melody_dict:
        
    def __init__(self, note=None, note_idx=None):        
        
        default_note = 'C4'
        
        if note in sound_dict.keys():
            self.note = note # frequency in Hz
            self.freq = freq_dict[note]
            self.sound = sound_dict[note] 
            self.wav_file = sound_path_dict[note]
        elif note is None and note_idx in range(len(scale)):
            self.note = scale[note_idx] # frequency in Hz
            self.freq = freq_dict[self.note]
            self.sound = sound_dict[self.note] 
            self.wav_file = sound_path_dict[self.note]
        else:             
            print('Unknown input {}, setting to {}'.format(note,default_note))
            self.note = default_note
            self.freq = freq_dict[note]
            self.sound = sound_dict[note]
            self.wav_file = sound_path_dict[note]

#%%
class music_theme:
    def __init__(self, theme='pop'):        
        self.theme = theme.lower() 
        default_theme = 'pop'
        
        if self.theme == 'somber':
            self.chords = [5,1,2,5] # Am Dm Em Am
            self.bpm = 55
        elif self.theme == 'cheerful':
            self.chords = [0,3,4,0] # C F G C
            self.bpm = 75
        elif self.theme == 'pop':
            self.chords = [0,4,5,3] # C G Am F
            self.bpm = 70
        elif self.theme == 'hip-hop':
            self.chords = [5,5,3,3] # Am Am F F
            self.bpm = 64
        else:
            print('Unknown input theme {}\nSetting to default {}'.format(self.theme,default_theme)) 
            self.theme = default_theme
            self.chords = [0,4,5,3]
            self.bpm = 70
            
#%% Try to combine into class

class note_class:
    
    fs = 44100  # Sampling frequency in Hz
    
    def __init__(self, note, instr='piano'):        
        #self.f0 = f0 # frequency in Hz
        self.note = note # Example C4
        self.f0 = freq_dict[note]
        self.instr = instr
        self.sound = sound_dict[note]