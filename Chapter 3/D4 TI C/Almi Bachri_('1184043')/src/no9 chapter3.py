# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 00:02:14 2019

@author: lovo
"""

def printNPMDijitGanjil(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 != 0):
            print(n, end = "")

printNPMDijitGanjil(input("Masukan NPM anda: "))