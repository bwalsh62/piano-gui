# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 13:45:35 2020

Speech recognition test

@author: Ben Walsh
for liloquy
"""

#%% Import libraries

# Custom Liloquy library to interpret text to music commands
from text2music import text2music

# Open source library to recognize speech
import speech_recognition as sr

# Open source library to access sound device to record
import sounddevice as sd

# Open source library to write wav files
from scipy.io.wavfile import write

# Built-in library timer
import time

#%% Define inputs and outputs
speech_file_recorded = "./record_speech_test.wav"

#%% Functions [in other modules but all in one place for testing]

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

def record_music(rec_notes_total, note_len_time, fs=44.1e3):
    
    # Samples in a note = the samples/second * time   
    note_len_n_samples = int(fs * note_len_time)
    
    # Record for data points = number of notes * data points / note
    recorded_sound = sd.rec(rec_notes_total*note_len_n_samples, samplerate=fs, channels=2)

    # Visualize timer while recording
    record_timer_viz(note_len_time,rec_notes_total)

    return recorded_sound

#%% Record speech
fs=44100

data = record_music(rec_notes_total=5, note_len_time=1, fs=fs)

write(speech_file_recorded, fs, data)

#%% Recognizer class

speech_file_test = r"C:\Users\benja\OneDrive\Documents\Python\liloquy-git\piano-gui\Pop_background_D.wav"
r = sr.Recognizer()

speech_in = sr.AudioFile(speech_file_recorded)
with speech_in as source:
    audio = r.record(source)

text_interpreted = r.recognize_google(audio)

#%% Print result
print('Interpreted speech file: {}\n'.format(speech_file_recorded))
print('Interpreted text:\n{}\n'.format(text_interpreted))

#%% Input into text_input

print('Running text2music... \n')
text2music(input_command = text_interpreted)