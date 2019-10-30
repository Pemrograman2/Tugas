# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 21:21:55 2019

@author: Asus
"""

def printNPMPerkalian(npm):
    npm = list(map(int, npm))
    hasil = 0
    for x in npm:
        hasil *= x
    
    print(hasil)
    
printNPMPerkalian(input("Masukan NPM anda: "))