# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 06:55:12 2019

@author: ANIF
"""

def printperkalian(npm):

    npm = list(map(int, npm))
    hasil = 0
    for n in npm:
        hasil *= n 
    print(hasil)

printperkalian(input("Masukkan NPM Anda: "))