# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 03:59:06 2019

@author: acer
"""

def X(npm):

    npm = list(map(int, npm))
    hasil = 0
    for n in npm:
        hasil *= n 
    print(hasil)

X(input("Masukkan NPM Anda: "))