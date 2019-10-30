# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 21:15:45 2019

@author: Asus
"""

def printNPMPenjumlahan(npm):
    npm = list(map(int, npm))
    hasil = 0
    for x in npm:
        hasil += x
    
    print(hasil)
    
printNPMPenjumlahan(input("Masukan NPM anda: "))