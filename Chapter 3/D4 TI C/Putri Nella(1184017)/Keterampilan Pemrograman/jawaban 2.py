# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 17:59:44 2019

@author: Putri Nella
"""

def npm2(npm):
    npm=int(npm)
    TwoLastDigit=abs(npm)%100
    for i in range(TwoLastDigit):
       print("Hallo, ", npm, " apa kabar ?")