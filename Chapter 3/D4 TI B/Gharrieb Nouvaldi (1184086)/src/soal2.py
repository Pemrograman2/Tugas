# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 22:33:00 2019

@author: Azure
"""

def soal2(npm):
    npm=int(npm)
    TwoLastDigit=abs(npm)%100
    for i in range(TwoLastDigit):
       print("Halo, ", npm, " apa kabar ?")