# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 23:44:11 2020

@author: Silas
"""

import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
import numpy as np
import os

os.chdir("..")
sample_rate, samples = wavfile.read('wavData/Tue-Sep-01-16-49.wav') #does the file IO so we know sample rate and samples based on wave PCM (16bit)
frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate, nfft = 2048, scaling = 'density') #does the FTT to break discrete wave into frequencies 

maxamp = abs(max(samples))/32767 #This block shows the max dbFS in the recording ( note dbfs supported from 0 to -inf where 0 is the highest)
max_dB = 20 * np.log10(maxamp)
print("max dBFS: %.2f" % max_dB)

plt.pcolormesh(times, frequencies, np.log(spectrogram)) #graphs the color of 3rd value at the position of time and frequency on the graph

    
dbfsPerFreq = (20 * np.log10( 2 * np.abs(spectrogram) / 2048)) - 96 #Takes the electric spectral density in v**2/hz and converts to dbFS. Had to convert FFT to length 2048 instead of tukey default 


maskedDbArr = np.ma.masked_invalid(dbfsPerFreq) #ignores -inf values associated with no sound recorded

avg_db_per_freq = np.apply_along_axis(np.mean, axis=1, arr=maskedDbArr) #takes 2d array and calculates average for EVERY list corresponding to a frequency bin (running into memory problems)

plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()

