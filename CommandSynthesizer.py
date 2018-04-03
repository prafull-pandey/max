#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 01:31:49 2018

@author: praf
"""

class CommandSynthesizer():
    entityFile='Entities.prop'
    entityDict={}
    def __init__(self):
        self._response=0
        self.entityParser()
        
        
    def entityParser(self):
        try:
            f=open(self.entityFile,'r')
        except IOError:
            print ("Could not read file:", self.entityFile)
        if f.mode == 'r':
            lines=f.readlines()
            for line in lines:
                k,v=line.split(':')
                v=v.split(',')
                self.entityDict[k]=v
        f.close()
"""        
        for k in self.entityDict:
            print(k+' : '+' '.join(self.entityDict[k]))
            
if __name__=="__main__":
    CommandSynthesizer=CommandSynthesizer('sdsds','sdsd')
    CommandSynthesizer.entityParser()
"""
    def synthesisCommand(self, command):
        for word in command.split():
            entity=searchWordInEntity(word)
            if entity not None:
                print('found entity '+entity)
        return entity
            
    def searchWordInEntity(self, word):
        for k in self.entityDict:
            if word in self.entityDict[k]:
                return k
        return None
        