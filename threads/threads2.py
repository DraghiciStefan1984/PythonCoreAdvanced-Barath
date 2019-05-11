# -*- coding: utf-8 -*-
"""
Created on Sat May 11 08:11:12 2019

@author: Stefan Draghici
"""

from threading import Thread, Lock

class BookMyBus:
    def __init__(self, available_seats):
        self. available_seats= available_seats
        self.lock=Lock()
        
    def buy(self, seats_requested):
        self.lock.acquire()
        if(self.available_seats>seats_requested):
            print('Confirming a seat')
            print('Processing payment')
            print('Printing a ticket')
            self.available_seats-=seats_requested
        else:
            print('No sets available')
        self.lock.release()
        
obj=BookMyBus(5)

t1=Thread(target=obj.buy, args=(3,))
t2=Thread(target=obj.buy, args=(1,))
t3=Thread(target=obj.buy, args=(4,))
t1.start()
t2.start()
t3.start()