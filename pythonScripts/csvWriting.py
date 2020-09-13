# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 23:06:45 2020

@author: Silas
"""
import csv
import os
os.chdir('..')

def appendMain():
    outputFile = open("csvData/main.csv", "a", newline = "") #newline arguments avoids doublespace; creates object to pass to writer object; a specifies append, w specifies overwrite
    outputWriter = csv.writer(outputFile) #creates object to allow to writerows 
    outputWriter.writerow([time,filename,low,mid,high])
    outputFile.close()