# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 19:08:30 2019

@author: Lenovo
"""
def soal2(npm):
    npm=int(npm)
    TwoLastDigit=abs(npm)%100
    for i in range(TwoLastDigit):
       print("Halo, ", npm, " apa kabar ?")