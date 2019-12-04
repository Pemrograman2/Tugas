# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 00:05:40 2019

@author: Aditya Luthfi
"""

def npm2(npm):
    npm = input("masukan npm : ") 
    key = int(npm)%100
    for i in range(key): 
        print("Halo" ,npm, "Apa Kabar?")
npm2(npm)