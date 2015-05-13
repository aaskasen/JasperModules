# -*- coding: utf-8-*-
import random
import re
import os
import subprocess

WORDS = ["BALCONY"]

def handle(text, mic, profile):
    """
        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """

    balcony_temp = subprocess.check_output("/opt/homeautomation/tdtool-with-sensors.py --sensor-data 3268102 |  awk 'FNR == 1 {print $3}'", shell=True)
    balcony_humi = subprocess.check_output("/opt/homeautomation/tdtool-with-sensors.py --sensor-data 3268102 |  awk 'FNR == 2 {print $3}'", shell=True)

    mic.say('Current temperature on the balcony is ' + balcony_temp + ' degrees celcius, current humidity is ' + balcony_humi + ' percent.')

def isValid(text):
    if re.search(r'\bBALCONY\b', text, re.IGNORECASE):
        return True
    else:
        return False
