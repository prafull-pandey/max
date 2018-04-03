#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 22:32:26 2018

@author: Prafull Pandey
"""
from SpeechToTextEngineInitialize import SpeechToTextEngineInitialize
from STTOutputController import STTOutputReader
from SubController import STTOutController

from queue import Queue


class MainController():
    
    #sttType
    sttEngineType='pocketsphinx'
    controllerName='PRAFULL'.upper()
    
    def controller(self):
        # Starting stt subprocess
        
        if self.sttEngineType=='pocketsphinx':
           commandArgs = self.pocketsphinxSTTInitialize()
        else:
            raise Exception(self._sttEngineType+': Speech to Text Engine not Supported')
        
        speechToTextEngineInitialize=SpeechToTextEngineInitialize(self.sttEngineType, commandArgs)
        sttProcessObj=speechToTextEngineInitialize.startSubProcess()
        #Initialization and start of Speech to Text Engine Ended
        
        #Initialization and start of stt output reader starts
        sttOutQueue=Queue() #store the output of stt Engine
        sttOutQueue.join()
        
        
        sttOutputReader=STTOutputReader(sttProcessObj,sttOutQueue)
        sttOutputReader.start()
        
        sttOutController=STTOutController(sttProcessObj,sttOutQueue,self.controllerName)
        sttOutController.start()
        
        
        
        
    def pocketsphinxSTTInitialize(self):

        # Arguments for initializing speech to text Engine
        dictAttribute=['-dict','/home/praf/Projects/modelFiles/7930.dic']
        lmAttribute=['-lm','/home/praf/Projects/modelFiles/7930.lm']
        inmicAttribute=['-inmic','yes']
        logAttribute=['-logfn', '/dev/null']
        sttArguments = inmicAttribute + dictAttribute + lmAttribute + logAttribute
        
        return sttArguments