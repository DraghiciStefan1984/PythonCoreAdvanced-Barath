# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:19:40 2019

@author: Stefan Draghici
"""

class Product:
    def __init__(self):
        self.name=''
        self.description=''
        self.price=0.0
        
        
p1=Product()
p1.name='p1'
p1.description='first product'
p1.price=23.2


class Course:
    def __init__(self, name, ratings):
        self.name=name
        self.ratings=ratings
        
    def average(self):
        return sum(self.ratings)/len(self.ratings)
        
c1=Course('coding', [3,4,5])
print(c1.average())


class Programmer:
    def __init__(self):
        self._name=''
        self._salary=0.0
        self._technologies=[]
        
    def getname(self, name):
        self._name=name
        
    def getsalary(self, salary):
        self._salary=salary
        
    def gettechnologies(self, technologies):
        self._technologies=technologies