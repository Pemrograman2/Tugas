# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 23:27:12 2019

@author: Ahmad Agung Tawakkal
"""

def NPM2(npm):
    npm = int (npm)
    Tld=abs(npm)%100
    for i in range(Tld):
        print ("Hallo, ",npm," apa kabar ?")

NPM2(npm)