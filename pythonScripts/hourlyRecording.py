# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 20:58:10 2020

@author: Silas
"""

import sounddevice as sd
from scipy.io.wavfile import write
import os
fs = 48000
sd.default.channels = 1
os.chdir("..")



def bugCorder(outFile, duration):
    print("starting the recording!")
    myrecording = sd.rec(int(duration * fs))
    sd.wait(duration + 5)
    write(outFile, fs, myrecording)
    print("write successful")



