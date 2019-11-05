# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 06:55:11 2019

@author: ANIF
"""

def printpenjumlahan(npm):

    npm = list(map(int, npm))
    hasil = 0
    for n in npm:
        hasil += n 
    print(hasil)

printpenjumlahan(input("Masukkan NPM Anda: "))