# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:55:36 2019

@author: Stefan Draghici
"""

global_var=123

def avg(a, b):
    return (a+b)/2

def avg2(*args):
    return sum(args)/len(args)

def calcs(a, b):
    return a+b, a-b, a*b, a/b

def display_global():
    print(global_var)
    
def display_global2():
    global_var=0
    print(global_var)
    print(globals()['global_var'])
    
print(global_var)
display_global2()

def display(name):
    def message():
        return 'hello '
    result=message()+name
    return result

print(display('Stefan'))

def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)