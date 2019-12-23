# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:28:27 2019

@author: Ben Walsh
For Liloquy

wav_file_clip(time_length, wav_file_input, wav_file_output)
    time_length = time in seconds to clip .wav file
    wav_file_input = path to .wav file desired to be shorteneed
    wav_file_output = new name of .wav file
    If no wav_file_output, assumed <wav_file_name>_clipped.wav

# TO DO
- add error checking to wav_file_clip

"""
#%% Import libraries

import wave
from os.path import exists

#%% Shorten input wav file
def wav_file_clip(t_len,wav_file_in,wav_file_out=None):
    
    # If no output name, supplied, use input name with _clipped suffix
    if wav_file_out==None:
        wav_file_out = wav_file_in[:-4]+'_clipped.wav'
        
    # ADD error checking to wav_file_in existence
    # Right now prints message but doesn't do anything
    if not(exists(wav_file_in)):
        print('Input file does not exist:'+wav_file_in)
        
    # Open wav file to read
    obj = wave.open(wav_file_in,'r')

    # Get sampling rate
    fs = obj.getframerate() 
    # Get other parameters to replicate in new file
    n_channels = obj.getnchannels()
    samp_width = obj.getsampwidth()
    
    # Based on fs, get number of frames for input time length
    n_frames = int(fs*t_len)
    
    # ADD error checking that t_len is shorter than actual time length
    # Right now prints message but doesn't do anything
    if n_frames > obj.getnframes():
        print('Desired output time length is longer than wav file length')
        # Could add 0s instead
        
    ## For debugging
#    print( "Number of channels",obj.getnchannels())
#    print ( "Sample width",obj.getsampwidth())
#    print ( "Frame rate.",obj.getframerate())
#    print ("Number of frames",obj.getnframes())
#    print ( "parameters:",obj.getparams())
    frames_read = obj.readframes(n_frames)
    obj.close()
    
    # Open new wav file
    obj = wave.open(wav_file_out,'wb')
    obj.setnframes(n_frames)
    obj.setnchannels(n_channels)
    obj.setsampwidth(samp_width)
    obj.setframerate(fs)
    obj.writeframes(frames_read) 
    obj.close()
        
    return wav_file_out

#%% Append two wav files into new file

def wav_file_append(wav_file1,wav_file2,merge_name='./appended.wav'):
    
    # ADD error checking to wav_file_in existence
    if not(exists(wav_file1)):
        print('Input file does not exist:'+wav_file1)
    if not(exists(wav_file2)):
        print('Input file does not exist:'+wav_file2)
    
    # Read first wav file
    obj = wave.open(wav_file1,'r')
    n_frames1 = obj.getnframes()
    wav1_data = obj.readframes(n_frames1)
    n_channels = obj.getnchannels()
    samp_width = obj.getsampwidth()
    fs = obj.getframerate()
    obj.close()

    # Read second wav file
    obj = wave.open(wav_file2,'r')
    n_frames2 = obj.getnframes()
    wav2_data = obj.readframes(n_frames2)
    obj.close()
    
    # Write new wav file
    obj = wave.open(merge_name,'wb')
    obj.setnframes(n_frames1+n_frames2)
    obj.setnchannels(n_channels)
    obj.setsampwidth(samp_width)
    obj.setframerate(fs)
    obj.writeframes(wav1_data+wav2_data) 
    obj.close()
        
    return merge_name

