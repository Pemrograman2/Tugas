# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 00:00:33 2019

@author: lovo
"""

def printNPMDijitGenap(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 == 0):
            if(n != 0):
                print(n, end = "")
                
printNPMDijitGenap(input("Masukan NPM anda: "))