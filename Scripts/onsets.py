import librosa
import librosa.display
import soundfile as sf
import os
import matplotlib.pyplot as plt
import numpy as np

y, sr = librosa.load("/Volumes/Workspace/wc/SeniorWork/BeldenFalls.9.12/audio/onsets.wav")
D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref = np.max)
img = librosa.display.specshow(D,y_axis = 'linear', x_axis = 'time', sr = sr)

plt.plot()

onsets = []

onsets = librosa.onset.onset_detect(y)

print(onsets)
print(onsets.shape)
