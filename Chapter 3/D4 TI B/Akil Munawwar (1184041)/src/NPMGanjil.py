# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 21:27:50 2019

@author: Asus
"""

def printNPMGanjil(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 != 0):
            print(n, end = "")
    
printNPMGanjil(input("Masukan NPM anda: "))