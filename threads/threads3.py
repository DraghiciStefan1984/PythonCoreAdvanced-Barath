# -*- coding: utf-8 -*-
"""
Created on Sat May 11 08:40:11 2019

@author: Stefan Draghici
"""

from threading import *
from time import *

class Producer:
    def __init__(self):
        self.products=[]
        #self.ordersplaced=False
        self.condition=Condition()
        
    def produce(self):
        self.condition.acquire()
        for i in range(1, 5):
            self.products.append('Product'+str(i))
            sleep(1)
            print('Item added')
        self.condition.notify()
        self.condition.release()
        #self.ordersplaced=True
        

class Consumer:
    def __init__(self, prod:Producer):
        self.prod=prod
        
    def consume(self):
        self.prod.condition.acquire()
        self.prod.condition.wait(timeout=0.2)
        self.prod.condition.release()        
        print('orders shipped ',self.prod.products)

        
p=Producer()
c=Consumer(p)

t1=Thread(target=p.produce)
t2=Thread(target=c.consume)
t1.start()
t2.start()