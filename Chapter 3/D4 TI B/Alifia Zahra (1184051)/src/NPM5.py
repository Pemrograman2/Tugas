# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 03:55:27 2019

@author: acer
"""

def x(npm):

    npm = list(map(int, npm))  
    for n in npm:
        print(n)

x(input("Masukkan NPM Anda: "))