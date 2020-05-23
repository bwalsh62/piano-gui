# -*- coding: utf-8 -*-
"""

Updated GUI with simpler interface

Created on Sat May 23 09:54:29 2020

@author: Ben Walsh
for liloquy
Copyright Benjamin Walsh 2020

"""

#%% Import libraries

from tkinter import Tk, Label, Button, Scale, Frame, Entry, PhotoImage, ttk, OptionMenu, Checkbutton, StringVar, IntVar
import os

#import gui_config
# from gui_config import play_cfg, main_cfg

#%% Define constants

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 500
MENU_HEIGHT = 100

#%% Initialize GUI

root = Tk()
root.title('liloquy - find your song')
root.geometry('{}x{}'.format(300, SCREEN_HEIGHT))

# Create main frame containers
#------------

main_frame = Frame(root, bg='brown', width=SCREEN_WIDTH, height=SCREEN_HEIGHT-MENU_HEIGHT, pady=166, padx=116)
#main_frame = Frame(root, bg='brown', width=main_cfg.width, height=main_cfg.height-MENU_HEIGHT, pady=main_cfg.pady, padx=main_cfg.padx)
menu_frame = Frame(root, bg='gray', width=SCREEN_WIDTH, height=MENU_HEIGHT, padx=2, pady=2)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

main_frame.grid(row=0)
menu_frame.grid(row=1, sticky="ew")

#%% Play button

#'play'
#img_file = "./icons/PlayIcon.png"
#width = 36
#height = 36
#grid_col = 0
#grid_row = 0

# Picture for play button
play_img_file = "./icons/PlayIcon.png"
if not(os.path.exists(play_img_file)):
    print(f'Cannot find: {play_img_file}')
    
photo = PhotoImage(file=play_img_file)
 
# Resizing image to fit on button 
play_img = photo.subsample(4) 

play_music_btn = Button(main_frame, width=60, height=60,text="Play",  image=play_img) #command=play_music,
#play_music_btn = Button(main_frame, width=play_cfg.width, height=play_cfg.height,text="Play", command=play_music, image=play_cfg.img)

play_music_btn.grid(column=0, row=0)
# play_music_btn.grid(colum = play_cfg.grid_col, row = play_cfg.grid_row)

#%% Run GUI

root.mainloop()