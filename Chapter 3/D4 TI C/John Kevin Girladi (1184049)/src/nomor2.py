# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 22:16:49 2019

@author: ASUS
"""

def npm(npm):
npm=int(input("input NPM : "))
DuaDigitTerakhir=abs(npm)%100
for i in range(DuaDigitTerakhir):
    print("Halo, ", npm, " Apa Kabar ?")