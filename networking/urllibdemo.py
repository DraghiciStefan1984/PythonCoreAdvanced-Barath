# -*- coding: utf-8 -*-
"""
Created on Sat May 11 09:07:57 2019

@author: Stefan Draghici
"""

import urllib.request as req

try:
    url=req.urlopen('https://www.python.org/')
    content=url.read()
except urllib.error.HTTPError:
    print('error')
    exit()
    
with open('python.html', 'wb') as f:
    f.write(content)
    