# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 20:56:26 2019

@author: benja

Music from: http://theremin.music.uiowa.edu/MISpiano.html

# TO DO
# - Try as a class
# - Add all sharps

"""
from pygame import mixer
#from os import getcwd

mixer.init()

# Paths to piano wav files
music_fpath = "./music_files/piano/"
C_path = music_fpath+"Piano.mf.C4_3s.wav"
#print('C_path ='+C_path)
#print('Current wd = '+getcwd())
Csharp_path = music_fpath+"Piano.mf.Db4_2p5s.wav"
D_path = music_fpath+"Piano.mf.D4_3s.wav"
Dsharp_path = music_fpath+"Piano.mf.Eb4_2p5s.wav"
E_path = music_fpath+"Piano.mf.E4_3s.wav"
F_path = music_fpath+"Piano.mf.F4_2p5s.wav"
Fsharp_path = music_fpath+"Piano.mf.Gb4_2p5s.wav"
G_path = music_fpath+"Piano.mf.G4_2p5s.wav"
Gsharp_path = music_fpath+"Piano.mf.Db4_2p5s.wav"
A_path = music_fpath+"Piano.mf.A4_3s.wav"
Asharp_path = music_fpath+"Piano.mf.Db4_2p5s.wav"
B_path = music_fpath+"Piano.mf.B4_2p5s.wav"

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

