# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 16:39:52 2020

@author: Silas
"""

import json, requests

url = 'https://www.purpleair.com/data.json?show=47497&key=K4BMD0QYYCHCYXBV'

def getPurple():
    response = requests.get(url) #goes and downloads from internet
    response.raise_for_status() #raises errors if applicable
    weatherData = json.loads(response.text) #loads into python variable
    datalist = weatherData["data"]
    data = datalist[0]
    fields = weatherData['fields']
    res = {fields[i]: data[i] for i in range(len(fields))} 
    temp = res['Temperature']
    pressure = res['Pressure']
    humid = res['Humidity']
    pm25 = res['pm']
    results = [temp, pressure, humid, pm25]
    return results

