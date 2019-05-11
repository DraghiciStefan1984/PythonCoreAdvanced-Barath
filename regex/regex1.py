# -*- coding: utf-8 -*-
"""
Created on Sat May 11 07:33:33 2019

@author: Stefan Draghici
"""

import re

s="1 I have great ideas and will 3 put the to use, one idea  5 at a time, not all ideas at 8 the same time."

print(re.findall(r'a\w\w', s))
print(re.match(r'a\w\w', s))
print(re.findall(r'a\w{1,2}', s))
print(re.split(r'\d+', s))
print(re.sub(r'idea', 'plan', s))
print(re.search(r'^a\w', s))