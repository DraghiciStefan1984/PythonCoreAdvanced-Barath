# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:10:41 2019

@author: Stefan Draghici
"""

class BMW:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
        
    def start(self):
        print('BMW starting')
        

class ThreeSeries(BMW):
    def __init__(self, cruise_control, make, model, year):
        super().__init__(make, model, year)
        self.cruise_control=cruise_control
        
    def start(self):
        print('Series 300 starting')
        

class FiveSeries(BMW):
    def __init__(self, parking_assist, make, model, year):
        super().__init__(make, model, year)
        self.parking_assist=parking_assist
        
    def start(self):
        print('Series 500 starting')
        

t=ThreeSeries(True, 'Bmw', 'Series 300', 2016)
f=FiveSeries(True, 'Bmw', 'Series 500', 2018)
print(t.model)
print(f.model)
t.start()
f.start()