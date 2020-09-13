# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 00:00:28 2020

@author: Silas
"""
import hourlyRecording as hr
import getDBforHZ as get
import csv
import time
import getPurple as gp

def collectSample():
   curTime = time.strftime("%c",time.localtime(time.time()))
   curHour = int(time.strftime("%H",time.localtime(time.time())))
   curMin = int(time.strftime("%M",time.localtime(time.time())))
   if curMin > 30: 
       curHour = curHour + 1
   timeName = "wavData/"+time.strftime("%a-%b-%d-%H-%M",time.localtime(time.time()))+'.wav'
   hr.bugCorder(outFile = timeName, duration = 60) #Record and write wav Set recording duration here
    
   #analyse wav
   db = get.getDBforHZ(file = timeName, desiredHz = [3000,5000,7000], plot = True)
   
   #grab weather data
   weather = gp.getPurple()
   
    #add to csv
   outputFile = open("csvData/main.csv", "a", newline = "") 
   outputWriter = csv.writer(outputFile)
   outputWriter.writerow([curTime,
                          curHour,
                          db[0],
                          db[1],
                          db[2],
                          weather[0],
                          weather[1],
                          weather[2],
                          weather[3]])
   outputFile.close()
collectSample()