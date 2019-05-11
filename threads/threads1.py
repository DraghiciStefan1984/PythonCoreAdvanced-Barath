# -*- coding: utf-8 -*-
"""
Created on Sat May 11 07:33:33 2019

@author: Stefan Draghici
"""

import threading
from threading import Thread

main_thread_name=threading.current_thread().getName()
print(main_thread_name)


def display_numbers():
    i=0
    while(i<=10):
        print(i)
        i+=1
        
t=Thread(target=display_numbers)
t.start()


class MyThread(Thread):
    def run(self):
        i=0
        while(i<=10):
            print(i)
            i+=1
            
t=MyThread()
t.start()
