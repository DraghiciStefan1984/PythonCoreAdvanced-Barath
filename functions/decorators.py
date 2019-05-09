# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:02:56 2019

@author: Stefan Draghici
"""

def double_decorator(fn):
    def inner():
        result=fn()
        return result*2
    return inner

@double_decorator
def ret():
    return 8

print(ret())

def generator(x, y):
    while x<y:
        yield x
        x+=1

result=generator(2, 10)     
for i in result:
    print(i)