# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 23:09:05 2019

@author: Dinda Anik Masruro

"""
def npm2(npm):
    npm=int(npm)
    TwoLastDigit=abs(npm)%100
    for i in range(TwoLastDigit):
       print("Hallo, ", npm, " apa kabar ?")
