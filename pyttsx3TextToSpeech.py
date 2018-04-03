#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 02:01:28 2018

@author: praf
"""
import pyttsx3
class TextToSpeech():
    def __init__(self):
        self._engine = pyttsx3.init()
        
    def speakTheText(self, textToSpeak):
        self._engine.say(textToSpeak)
        self._engine.runAndWait()