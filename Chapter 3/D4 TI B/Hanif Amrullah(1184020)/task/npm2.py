# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 07:06:58 2019

@author: Hanif Amrullah
"""

def npm2(npm):
    npm=int(npm)
    TwoLastDigit=abs(npm)%100
    for i in range(TwoLastDigit):
       print("Halo, ", npm, " apa kabar ?")