# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 21:24:20 2019

@author: Asus
"""

def printNPMGenap(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 == 0):
            if(n != 0):
                print(n, end = "")
    
printNPMGenap(input("Masukan NPM anda: "))