# -*- coding: utf-8 -*-
"""
JUST THE AVG DBFS PER FREQ
Created on Sat Aug 29 12:49:17 2020

@author: Silas
"""
from scipy import signal
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir("..")
file = "sampleAudio/Sun-Aug-30-10-47.wav" #place file here
tolerance = 500 
desiredHz = 5000

sample_rate, samples = wavfile.read(file)
frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate, nfft = 2048, scaling = 'density')
dbfsPerFreq = (20 * np.log10( 2 * np.abs(spectrogram) / 2048)) - 96
maskedDbArr = np.ma.masked_invalid(dbfsPerFreq)
roundedMaskedDbArr = np.around(maskedDbArr, decimals = 7)
avg_db_per_freq = np.apply_along_axis(np.mean, axis=1, arr=roundedMaskedDbArr)

plt.plot(frequencies, avg_db_per_freq)
plt.axis([0, 22000,-500, 0 ])
plt.xlabel("Frequency (Hz)")
plt.ylabel("dbFS")
plt.title(file)


