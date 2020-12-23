import librosa
import librosa.display
import soundfile as sf
import os
import matplotlib.pyplot as plt
import numpy as np
from pydub import AudioSegment
from ffmpy import FFmpeg


def extract_clips(filepath):
    """creates directory on OS that contains extracted samples from audio clip"""

    y, sr = librosa.load(filepath)
    y_harmonic, y_percussive = librosa.effects.hpss(y)
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y_percussive)), ref = np.max)
    #img = librosa.display.specshow(D,y_axis = 'linear', x_axis = 'time', sr = sr)
    print("loaded audio")

    #with backtrack
    onsets = []

    #no backtrack
    onsetsnb = []

    onsets = librosa.onset.onset_detect(y_percussive, backtrack = True, units = 'time')
    onsetsnb = librosa.onset.onset_detect(y_percussive, units = 'time')

    #make a directory for noise clips extracted from ambient
    directory = "/Users/wconrad/Desktop/seniorproject/sounds"

    if(not(os.path.isdir(directory))):
        os.mkdir(directory)

    #write noises to new directory
    i = 1
    for onset in onsetsnb:
        current_sample, sr = librosa.load(filepath, offset = onset, duration = .25)
        sf.write(directory + f'/noise{i}.wav', current_sample, sr)
        i+=1
    
    return






#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#write a sound evaluator function
#to select and augment best rhythmic clips
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def rhythm_score(sound):
    """assigns score to rhythm sound,
    categorizes kick, snare, clap, etc"""

    #do cool stuff...


#works for uniform 16th notes
#next step: how can we vary the notes that are added (in one function)
#we could create multiple functions that are called at different times

def create_beatmap(bpm, length):
    """creates a timemap of rhythmic onset events"""
    
    beatmap = []
    
    bps = bpm / 60.0

    tbw = 1 / bps
    tbh = tbw / 2.0
    tbq = tbh / 2.0
    tbs = tbq / 2.0
    
    notefreqs = [tbw, tbh, tbq, tbs]
    
    iters = int(length/tbs)
    
    for i in range(iters):
        time = i * tbs
        beatmap.append(time)
            
    return beatmap




def half_anda(bpm, noise1, noise2):
    noise1 = AudioSegment.from_wav('./rhythmcomps/noise3.wav')
    noise2 = AudioSegment.from_wav('./rhythmcomps/noise23.wav')

    sliced1 = noise1[:250]
    sliced2 = noise2[:250]

    combined = sliced1 + sliced2
    half_anda = combined * 20

    half_anda.export('../components/half_anda.wav', format='wav')

    return

def quarter(bpm, noise):
    """creates quarter notes with noise"""

    noise = AudioSegment.from_wav('./rhythmcomps/noise17.wav')


    noise = noise[:250]

    seconds = 30

    quarter = noise * 4 * 2 * seconds

    quarter.export('../components/quarter.wav', format='wav')

    return

def sixteenths(bpm, noise):
    """creates sixteenth notes with noise"""

    noise4 = AudioSegment.from_wav('./rhythmcomps/noise63.wav')

    sliced4 = noise4[:125]

    sixteenths = sliced4 * 16 * 10

    sixteenths.export('../components/sixteenths.wav', format = 'wav')

    return


def beat1(bpm, half_anda, sixteenths, quarters):
    
    half_anda = AudioSegment.from_wav('../components/half_anda.wav')
    quarters = AudioSegment.from_wav('../components/quarter.wav')

    half_anda = half_anda[:250]
    quarters = quarters[:10000]
    quarters = quarters + 12

    plus_sixteenths = noise3.overlay(sixteenths)
    plus_quarters = plus_sixteenths.overlay(quarters)

    extended = plus_quarters * 5

    extended.export('../components/beatwquarters.wav', format = 'wav')
    
    return
