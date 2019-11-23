# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 23:00:24 2019

@author: Asus
"""

def NPM2(npm):
    npm = int (npm)
    Tld=abs(npm)%100
    for i in range(Tld):
        print ("Hallo, ",npm," apa kabar ?")

NPM2(npm)