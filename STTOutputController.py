#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 00:19:30 2018

@author: Prafull Pandey

@Description
"""
import threading
"""
@ This thread is used for continously reading the output from STT Engine and store it in Queue
"""
class STTOutputReader(threading.Thread):
    def __init__(self, outprocess, outQueue):
        #assert isinstance(outqueue,Queue)
        #assert callable(fd.readline)
        threading.Thread.__init__(self)
        self._outprocess=outprocess
        self._outQueue=outQueue
        
    def run(self):
        while True:
            output = self._outprocess.stdout.readline()
            if output == '' and self._outprocess.poll() is not None:
                raise Exception('Speech to Text Engine Failed')
            if output:
                print('Line added: ',output.strip())
                #self._outQueue.put(output.strip().decode("utf-8"))
                self._outQueue.put(output.strip())
            
    def eof(self):
        return not self.is_alive() and self._outQueue.empty()