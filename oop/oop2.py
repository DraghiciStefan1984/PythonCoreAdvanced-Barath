# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:52:28 2019

@author: Stefan Draghici
"""

class Student:
    #static field
    major='CSE'
    count=0
    
    def __init__(self, roll_number, name):
        self.roll_number=roll_number
        self.name=name
        Student.count+=1
        
    @staticmethod
    def displayStudentCount():
        print('student object count is {}'.format(Student.count))
        
s1=Student(1, 'John')
s2=Student(2, 'Mike')
print(s1.major)
print(s1.count)
print(s2.major)
print(s2.count)
print(s1.displayStudentCount())