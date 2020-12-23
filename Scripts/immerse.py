import os

#take user input bpm

bpm = input("Enter a BPM value: ")

bpm = int(bpm)

print("Select audio clip")

import tkinter as tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

tk.Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

#get audio from user
#ambient_audio = input("Type ambient audio filepath: ")

#call onsets.py
from onsets import extract_clips
#make_rhythm(ambient_audio)
extract_clips(filename)

#create the timelapse from the footage
#uses lapse.py
from lapse import create_images

print("Select video clip")

tk.Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
footage = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)

#footage_dir = input("Type footage directory filepath: ")

print(os.getcwd())

create_images(footage)

from ffmpy import FFmpeg

#for each folder of images in directory..

framerate = input("Enter desired playback framerate: ")

ff = FFmpeg(
    inputs={'/Users/wconrad/Desktop/seniorproject/Vid/images/%d.jpg': f'-framerate {framerate} -y'},
    outputs={'/Users/wconrad/Desktop/components/vid.MP4':None}
)

ff.run()

#generate mood map

from moodmap import generate_moodmap

hsv_set = generate_moodmap()

mood = hsv_set[0]

#generate soundtrack

import create_sounds_basic
from create_sounds_basic import assign_color, assign_possible_notes, assign_fund, assign_harm, create_fund, create_harm, create_score

color = assign_color(round(mood[0]*360))
print(color)

possible_notes = assign_possible_notes(color)


fund = []

#happier image
if(mood[2] > .5):
    
    #define fundamental low chord
    for note in possible_notes['g']:
        
        i = 0
        if(note[-5] == "2"):

            fund.append(note[-6:-4])

#sadder image
else:
    #define fundamental low chord
    for note in possible_notes['g2']:
        
        i = 0
        if(note[-5] == "2"):
            
            fund.append(note[-6:-4])

print(fund)

from create_sounds import create_piano_notes

piano_notes = create_piano_notes()

fund_midi_notes = []

for note in fund:
    fund_midi_notes.append(piano_notes[note])

print(fund_midi_notes)




#fundamental = assign_fund(possible_notes, mood[2])
#fund = create_fund(fundamental, 20) #length is second param, to be specified by user
#mel = assign_harm(possible_notes, mood[2], mood[1])
#melody = create_harm(mel, mood[1], mood[2], 20)
#create_score(fund, melody)

#link score and video in adobe









