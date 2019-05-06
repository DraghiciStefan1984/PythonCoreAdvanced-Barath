# -*- coding: utf-8 -*-
"""
Created on Mon May  6 19:51:46 2019

@author: Stefan Draghici
"""

print('hello\n'*3)

numbers=[int(x) for x in input('enter three numbers:').split()]
s=0
for n in numbers:
    s+=n
print(s)