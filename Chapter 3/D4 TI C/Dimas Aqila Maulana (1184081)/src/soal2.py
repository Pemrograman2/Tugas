# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 20:17:23 2019

@author: dimas
"""

def npm2(npm):
    npm=int(npm)
    TwoLastDigit=abs(npm)%100
    for i in range(TwoLastDigit):
       print("Hallo, ", npm, " apa kabar ?")