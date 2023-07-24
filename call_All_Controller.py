#!/usr/bin/env python3
import time
from datetime import datetime, timedelta
import threading

while (1):
    try:
        start_time = time.time()
        exec(open("All_Controller4_BA.py").read())
        end_time = time.time()
        total_time = round(end_time - start_time)
        print('OK')
        time.sleep(300-total_time)
    except:
        time.sleep(150)
