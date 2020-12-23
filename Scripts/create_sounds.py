"""
Create a new MIDI file with some random notes.
The file is saved to test.mid.
"""
from __future__ import division
import random
import sys
from mido import Message, MidiFile, MidiTrack, MAX_PITCHWHEEL, second2tick

bass_file = MidiFile()

bass_track = MidiTrack()
bass_file.tracks.append(bass_track)

bass_track.append(Message('program_change', program=10))

beat = 480  #480 ticks/beat
#ticks_per_expr = int(sys.argv[1]) if len(sys.argv) > 1 else 20
for i in range(8):
    note = 36 #electric bass drum
    bass_track.append(Message('note_on', note=note, velocity=100, time=0))
    #for j in range(delta // ticks_per_expr):
    #    pitch = MAX_PITCHWHEEL * j * ticks_per_expr // delta
    #    track.append(Message('pitchwheel', pitch=pitch, time=ticks_per_expr))
    bass_track.append(Message('note_off', note=note, velocity=100, time=beat))

bass_file.save('./soundcomps/bass.mid')

#draw from offsets for higher rhythmic sounds
#import offsets
#important note: hihats only sound good if they start right on at the beginning
#feature for onset sound detector

hihat_file = MidiFile()

hihat_track = MidiTrack()
hihat_file.tracks.append(hihat_track)

hihat_track.append(Message('program_change', program=10))

hihats = [1,2,3]
hihat = random.choice(hihats)

hihats.remove(hihat)

accent1 = random.choice(hihats)
hihats.remove(accent1)

accent2 = random.choice(hihats)

sixteenth = 480//4  #480 ticks/beat
#ticks_per_expr = int(sys.argv[1]) if len(sys.argv) > 1 else 20
for i in range(64):

    #hihat
    hihat_track.append(Message('note_on', note=hihat, velocity=100, time=0))
    
    #coin flip: add accent on quarter note
    if(i%2 == 0 and random.choice([1,2]) == 2):
        acc = random.choice([accent1,accent2])
        hihat_track.append(Message('note_on', note=acc, velocity=100, time=0))
        hihat_track.append(Message('note_off', note=acc, time=sixteenth))
        
        #end other note too
        hihat_track.append(Message('note_off', note=hihat, velocity=100, time=0))
    else:
        hihat_track.append(Message('note_off', note=hihat, velocity=100, time=sixteenth))
        

hihat_file.save('./soundcomps/hihat.mid')


#rim
rim_file = MidiFile()

rim_track = MidiTrack()
rim_file.tracks.append(rim_track)

rim_track.append(Message('program_change', program=10))

for i in range(8):
    rim = 0
    rim_track.append(Message('note_on', note=rim, velocity=100, time=beat))
    rim_track.append(Message('note_off', note=rim, velocity=100, time=beat))

rim_file.save('./soundcomps/rim.mid')


#piano
#has to come from the chords chosen by the image color
def create_piano_notes():
    """create piano notes dictionary, MIDI mapping"""

    piano_notes = {}

    notes = ["a","a+","b", "c", "c+", "d","d+", "e", "f", "f+", "g", "g+"]
    octaves = ["0","1","2","3", "4", "5", "6", "7", "8"]

    octave = 0
    for i in range(1,89):
        key = notes[(i%len(notes))-1] + octaves[octave]
        piano_notes[key] = i
        if((i+9)%12 == 0):
            octave+=1

    return piano_notes

piano_notes = create_piano_notes()
print(piano_notes)

#fundamental chords

fund_file = MidiFile()

fund_track = MidiTrack()
fund_file.tracks.append(fund_track)

fund_track.append(Message('program_change', program=1))

fund1 = 43
fund4 = 47
fund6 = 38
fund12 = 55

for i in range(4):

    fund_track.append(Message('note_on', note=fund1, velocity=100, time=0))
    fund_track.append(Message('note_on', note=fund4, velocity=70, time=0))
    fund_track.append(Message('note_on', note=fund6, velocity=70, time=0))
    fund_track.append(Message('note_on', note=fund12, velocity=70, time=0))

    fund_track.append(Message('note_off', note=fund1, velocity=100, time=beat*4))
    fund_track.append(Message('note_off', note=fund4, velocity=70, time=0))
    fund_track.append(Message('note_off', note=fund6, velocity=70, time=0))
    fund_track.append(Message('note_off', note=fund12, velocity=70, time=0))

for i in range(4):

    fund_track.append(Message('note_on', note=fund1+3, velocity=100, time=0))
    fund_track.append(Message('note_on', note=fund4+3, velocity=70, time=0))
    fund_track.append(Message('note_on', note=fund6+3, velocity=70, time=0))
    fund_track.append(Message('note_on', note=fund12+5, velocity=70, time=0))

    fund_track.append(Message('note_off', note=fund1+3, velocity=100, time=beat*4))
    fund_track.append(Message('note_off', note=fund4+3, velocity=70, time=0))
    fund_track.append(Message('note_off', note=fund6+3, velocity=70, time=0))
    fund_track.append(Message('note_off', note=fund12+5, velocity=70, time=0))

fund_file.save('./soundcomps/fund.mid')


#ambient

amb_file = MidiFile()

amb_track = MidiTrack()
amb_file.tracks.append(amb_track)

fund_track.append(Message('program_change', program=1))

amb = fund1
oct1 = fund1+12

for i in range(4):
    amb_track.append(Message('note_on', note=amb, velocity=100, time=0))
    amb_track.append(Message('note_on', note=oct1, velocity=100, time=0))

    amb_track.append(Message('note_off', notlse=amb, velocity=70, time=beat*4))
    amb_track.append(Message('note_off', note=oct1, velocity=70, time=0))

for i in range(4):
    amb_track.append(Message('note_on', note=amb+3, velocity=100, time=0))
    amb_track.append(Message('note_on', note=oct1+5, velocity=100, time=0))

    amb_track.append(Message('note_off', note=amb+3, velocity=70, time=beat*4))
    amb_track.append(Message('note_off', note=oct1+5, velocity=70, time=0))


amb_file.save('./soundcomps/amb.mid')


"""
fund_file = MidiFile()

fund_track = MidiTrack()
fund_file.tracks.append(fund_track)

fund_track.append(Message('program_change', program=1))

fund1 = 48
fund3 = 50
fund5 = 52

g1 = 60
g3 = 62
g5 = 64

for i in range(4):

    fund_track.append(Message('note_on', note=fund1, velocity=100, time=0))
    fund_track.append(Message('note_on', note=fund3, velocity=70, time=0))
    fund_track.append(Message('note_on', note=fund5, velocity=70, time=0))

    fund_track.append(Message('note_off', note=fund1, velocity=100, time=beat*4))
    fund_track.append(Message('note_off', note=fund3, velocity=70, time=0))
    fund_track.append(Message('note_off', note=fund5, velocity=70, time=0))

for i in range(4):

    fund_track.append(Message('note_on', note=g1, velocity=100, time=0))
    fund_track.append(Message('note_on', note=g3, velocity=70, time=0))
    fund_track.append(Message('note_on', note=g5, velocity=70, time=0))

    fund_track.append(Message('note_off', note=g1, velocity=100, time=beat*4))
    fund_track.append(Message('note_off', note=g3, velocity=70, time=0))
    fund_track.append(Message('note_off', note=g5, velocity=70, time=0))


fund_file.save('./soundcomps/fund.mid')
"""





