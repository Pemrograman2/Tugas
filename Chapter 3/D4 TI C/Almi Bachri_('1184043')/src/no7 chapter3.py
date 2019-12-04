# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 23:59:30 2019

@author: lovo
"""

def printNPMPerkalian(npm):
    npm = list(map(int, npm))
    hasil = 0
    for x in npm:
        hasil *= x

    print(hasil)

printNPMPerkalian(input("Masukan NPM anda: "))