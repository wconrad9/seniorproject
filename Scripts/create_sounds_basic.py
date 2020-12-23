#glob the files corresponding to our Grand Piano library of notes

import glob
import os

piano = glob.glob('../GrandPiano.cmaj/*.wav')

#We must (at this point) define a dictionary mapping a range of color values to a set of playable notes

#Our colors so far:
# Red
# Yellow
# Green
# Cyan
# Blue
# Magenta


#'Color' attributes:
# hue range
# playable notes

# value determines reverb, attack, release
# saturation determines pace, steps (of 'arp')

class color():
    def __init__(self, name, chords, hue_range):
        self = self
        self.name = name
        self.chords = chords
        self.hue_range = hue_range
    def toString():
        print(self.chords)
        print(self.name)
        print(self.hue_range)

#there will be a bug someday relating to the boundary between colors

red = color('red', {'c': ['c','d','e','b'], 'f': ['f','g','a','c','e']}, [[0, 50], [340,360]])
green = color('green', {'g': ['g','b','d','a'], 'g2': ['g','b','d','g']}, [80, 160])
yellow = color('yellow', {'sad': ['c','d','f','a'], 'f': ['f','a','c']}, [50, 80])
cyan = color('cyan', {'c': ['c','e','g','b'], 'g': ['g','b','c','e']}, [160, 180])
blue = color('blue', {'fear': ['e','a','c','e'], 'admiration': ['c','f','a','d']}, [180, 220])
magenta = color('magenta', {'-d': ['-d','g','b'], 'e': ['e','g','b']}, [245, 340])

#let's store these colors in a global list

colors = []
colors.append(red)
colors.append(green)
colors.append(yellow)
colors.append(cyan)
colors.append(blue)
colors.append(magenta)

                
def assign_color(hue_value):
    """This function determines which sound mapping should be applied
    to a specific mean hue value generated from an image."""
    
    assigned_color = ''
    
    for color in colors:
        
        #because red has two ranges, need an edge case
        if(color.name != 'red'):
            
            if(hue_value < color.hue_range[1] and hue_value > color.hue_range[0]):
                assigned_color = color
                
        else:
            
            #honestly assigned_color equals red if we get here...
            
            #because red has two ranges
            for span in color.hue_range:
                
                if(hue_value < span[1] and hue_value > span[0]):
                    assigned_color = color
    
    return assigned_color


def assign_possible_notes(color):
    """assigns possible notes for this color"""

    possible_notes = {}

    for chord in color.chords:
        
        #add dictionary key
        possible_notes[chord] = []
        
        for comp in color.chords[chord]:

            for note in piano:
                
                if note[19] == comp:
                    
                    #add notes as values for the chord key
                    possible_notes[chord].append(note)

    return possible_notes
    
#Use value and hue information to choose a progression of notes
#open question: how will the number of notes being played at once be determined?
def assign_fund(possible_notes, value):
    """creates a score determined by the aesthetic quality of an image"""
    
    from pydub import AudioSegment
    
    fund = []
    
    #happier image
    if(value > .5):
        
        #define fundamental low chord
        for note in possible_notes['g']:
            
            i = 0
            if(note[-5] == "2"):
                
                aud = AudioSegment.from_wav(note)
                aud = aud[:1000]
                
                fund.append(aud)

    #sadder image
    else:
        #define fundamental low chord
        for note in possible_notes['g2']:
            
            i = 0
            if(note[-5] == "2"):
                
                aud = AudioSegment.from_wav(note)
                aud = aud[:1000]
                
                fund.append(aud)
        
    return fund


def create_fund(fundamentals, length):
    """writes an output file with the notes determined by the image"""
    
    temp = fundamentals[0]
    
    for i in range(1, len(fundamentals)):
        temp = temp.overlay(fundamentals[i])
    
    temp = temp * length
    
    temp.export("../../programmed1.wav", format = 'wav')
    
    return temp

def assign_harm(possible_notes, value, saturation):
    """use the image to create a harmony to overlay on the fundamental chords"""
    
    import random
    from pydub import AudioSegment
    
    notes = set()
    
    melody = []
    
    #now randomly select one of each note to add to the melody
    random.shuffle(possible_notes['g'])
    
    len_mel = 0
    
    #this is hard coded at 'g' right now; try to determine with color
    for note in possible_notes['g']:
        
        #upper octaves
        if((note[-5] == "4" or note[-5] == "5")):
            
            
            notes.add(note[-6])
            if(len(notes) > len_mel):
                da = AudioSegment.from_wav(note)
                da = da[:500]
                melody.append(da)
            
            len_mel = len(melody)
            
    return melody

def create_harm(melody, saturation, value, length):
    """used to create the harmony"""
    
    import random
    
    temp1 = melody[0]
    
    for i in range(1, len(melody)):
        temp1 = temp1 + melody[i]
    
    temp1 = temp1 * (length//2)
    
    random.shuffle(melody)
    
    temp2 = melody[0]
    
    for i in range(1,len(melody)):
        temp2 = temp2 + melody[i]
    
    temp2 = temp2 * (length//2)
    
    mel = temp1 + temp2
    
    mel.export("../../mel.wav", format = 'wav')
    
    return mel
    
def create_score(fundamental, melody):
    """creates the completed score for one section of footage"""
    
    #chord intro
    intro = fundamental[:5000]
    
    #add mel1
    build1 = fundamental[:7500].overlay(melody[:7500])
    
    #build to shift
    tension = melody[7500:10000]
    
    #shift
    chorus2 = fundamental[:10000].overlay(melody[20000:30000])
    
    glue1 = intro + build1
    glue2 = glue1 + tension
    glue3 = glue2 + chorus2
    
    #fade_score = glue3.fade_in(1000).fade_out(5000)
    
    glue3.export("../../components/score1.wav", format = 'wav')

    
    
