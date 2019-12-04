# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 23:55:26 2019

@author: lovo
"""

def printNPMSatuPersatu(npm):
    npm = list(map(int, npm))  
    for n in npm:
        print(n)

printNPMSatuPersatu(input("Masukan NPM anda: "))