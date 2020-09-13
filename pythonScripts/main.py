# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 23:58:06 2020

@author: Silas
"""

import schedule
import collectSample
import time

schedule.every(19).minutes.do(collectSample.collectSample)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute