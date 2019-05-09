# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:00:54 2019

@author: Stefan Draghici
"""

class Student:
    '''
    def __init__(self):
        self.__id=0
        self.__name=''
        
    def display(self):
        print(self.__id, self.__name)
    '''
    
    def setId(self, val):
        self.id=val
        
    def setName(self, val):
        self.name=val
        
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def display(self):
        print(self.getId(), self.getName())
    
        
s=Student()
s.setId(34)
s.setName('Bob')
s.display()