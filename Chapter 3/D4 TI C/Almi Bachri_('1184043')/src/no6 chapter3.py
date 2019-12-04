# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 23:56:27 2019

@author: lovo
"""

def printNPMPenjumlahan(npm):
    npm = list(map(int, npm))
    hasil = 0
    for x in npm:
        hasil += x

    print(hasil)

printNPMPenjumlahan(input("Masukan NPM anda: "))