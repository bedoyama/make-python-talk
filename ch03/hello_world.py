#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 20:59:32 2024

@author: mauricio
"""

import speech_recognition as sr
speech = sr.Recognizer()
print('Python is listening...')
with sr.Microphone() as source:
    speech.adjust_for_ambient_noise(source)
    audio = speech.listen(source)
    inp = speech.recognize_google(audio)
print(f'You just said {inp}.') 