# -*- coding: utf-8 -*-
"""
Created on Mon May  6 19:24:36 2019

@author: Stefan Draghici
"""

s={1,3,2,5,3,2,1,3}
print(s)
s.update('test')
print(s)

f=frozenset(s)
print(f)