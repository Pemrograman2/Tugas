# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 22:42:16 2019

@author: ASUS
"""

def dijitgenap(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 == 0):
            if(n != 0):
                print(n, end = "")
                
dijitgenap(input("NPM: "))