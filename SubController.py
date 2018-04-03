#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 00:20:36 2018

@author: praf
"""
import threading
from pyttsx3TextToSpeech import TextToSpeech
from  CommandSynthesizer import CommandSynthesizer
import time

class STTOutController(threading.Thread):
    def __init__(self, outprocess, outQueue, name):
        #assert isinstance(outqueue,Queue)
        #assert callable(fd.readline)
        threading.Thread.__init__(self)
        self._outprocess=outprocess
        self._outQueue=outQueue
        self._name=name
        self._commandSynthesizer=CommandSynthesizer()
        
    def run(self):
        ttsEngine=TextToSpeech()
        while True:
            #print('itsRunning')
            if not self._outQueue.empty():
                line=self._outQueue.get()
                print('Read line: ',line)
                if self._name in line:
                    ttsEngine.speakTheText('Yes Sir, what can I do for you')
                    self._outQueue.task_done()  #Clears the remaining Queue
                    self._outprocess.stdout.flush() #Clears the stdout buffer
                    print('with due respect ask anything')
                    t_end = time.time() + 60 * 5    #5 sec timer for next command
                    while time.time() < t_end:
                        fullCommand=[]
                        if not self._outQueue.empty():
                            line=self._outQueue.get()
                            fullCommand.add(line)
                            print('Read line: ',line)
                            entity=self._commandSynthesizer.synthesisCommand(line)
                            if entity not None:
                                loadedModule=loadModule(entity)
                                
    def loadModule(self, entityName):
        className='modules'+'.'+entityName+'.'+entityName
        components = name.split('.')
        mod = __import__(components[0])
        for comp in components[1:]:
            mod = getattr(mod, comp)
        return mod
            
                            
                        