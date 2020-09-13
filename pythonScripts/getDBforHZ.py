# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 13:56:46 2020

@author: Silas
"""

from scipy import signal
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

def getDBforHZ(file, desiredHz, tolerance = 250, plot = False):
    desiredMetric = []
    sample_rate, samples = wavfile.read(file)
    frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate, nfft = 2048, scaling = 'density')
    dbfsPerFreq = (20 * np.log10( 2 * np.abs(spectrogram) / 2048)) - 96
    maskedDbArr = np.ma.masked_invalid(dbfsPerFreq)
    roundedMaskedDbArr = np.around(maskedDbArr, decimals = 7)
    avg_db_per_freq = np.apply_along_axis(np.mean, axis=1, arr=roundedMaskedDbArr)
    binsize = frequencies[1]
    for x in desiredHz:
        toleranceIndexDif = int(tolerance // binsize)
        indexForDesired = int(x // binsize)
        desiredArray = avg_db_per_freq[indexForDesired - toleranceIndexDif : indexForDesired + toleranceIndexDif]
        desiredMetric.append(np.mean(desiredArray))
    if plot:
        plt.plot(frequencies, avg_db_per_freq)
        plt.axis([0, 22000,-500, 0 ])
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("dbFS")
        plt.title(file)
    return(desiredMetric)

