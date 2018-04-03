#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 00:17:17 2018

@author: Prafull Pandey

@Description
    This module initializes the speech to text engine(stt) with the parameters, starts the subprocess and return the process object.
    
    Initialize the class first by type of stt and arguments as list
    
    Currently Supported Class Types
        1-pocketsphinx
"""

from subprocess import Popen, PIPE

class SpeechToTextEngineInitialize():
    def __init__(self, sttEngineType, commandArgs):
        self._sttEngineType=sttEngineType
        self._commandArgs=commandArgs
        
    def startSubProcess(self):
        if not self._sttEngineType:
            raise Exception('Speech To Text Engine Type not Initialized')
        if not self._commandArgs:
            raise Exception('No argumemts provided for Speech To Text Engine')
            
        if self._sttEngineType=='pocketsphinx':
            command=['pocketsphinx_continuous']
            command.extend(self._commandArgs)
            sttProcess=self.runSubProcess(command)
            return sttProcess
        else:
            raise Exception(self._sttEngineType+': Speech to Text Engine not Supported')
        
            
    def runSubProcess(self,command):
        process = Popen(command, stdout=PIPE, shell=False, universal_newlines=True)
        return process