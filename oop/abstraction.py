# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:10:41 2019

@author: Stefan Draghici
"""

from abc import abstractmethod, ABC

#make the class abstract
class BMW(ABC):
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
        
    def start(self):
        print('BMW starting')
        
    @abstractmethod
    def drive(self):
        pass
        

class ThreeSeries(BMW):
    def __init__(self, cruise_control, make, model, year):
        super().__init__(make, model, year)
        self.cruise_control=cruise_control
        
    def start(self):
        super().start()
        print('Series 300 starting, overload.')
        
    def drive(self):
        print('Series 300 drive.')
        

class FiveSeries(BMW):
    def __init__(self, parking_assist, make, model, year):
        super().__init__(make, model, year)
        self.parking_assist=parking_assist
        
    def start(self):
        print('Series 500 starting, override.')

    def drive(self):
        print('Series 500 drive.')        

t=ThreeSeries(True, 'Bmw', 'Series 300', 2016)
f=FiveSeries(True, 'Bmw', 'Series 500', 2018)
print(t.model)
print(f.model)
t.start()
f.start()
t.drive()
f.drive()