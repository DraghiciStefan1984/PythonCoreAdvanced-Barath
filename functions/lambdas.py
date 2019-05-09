# -*- coding: utf-8 -*-
"""
Created on Thu May  9 14:44:40 2019

@author: Stefan Draghici
"""

f1=lambda n:n**3
print(f1(3))

f2=lambda x: 'even' if x%2==0 else 'odd'
print(f2(3))

lst=[x for x in range(100)]
filtered_lst=filter(lambda x:x%2==0, lst)
print(list(filtered_lst))

mapped_lst=map(lambda x:x*2, lst)
print(list(mapped_lst))

from functools import reduce

reduced_lst=reduce(lambda x, y:x+y, lst)
print(reduced_lst)