# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 22:45:55 2019

@author: ASUS
"""

def dijitganjil(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 != 0):
            print(n, end = "")
dijitganjil(input("Masukan NPM anda: "))