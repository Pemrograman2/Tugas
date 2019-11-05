# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 14:23:05 2019

@author: ANIF
"""

#DigitGanjil
def printNPMDigitGanjil(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 != 0):
              print(n, end = "")
printNPMDigitGanjil(input("Masukan NPM anda :"))