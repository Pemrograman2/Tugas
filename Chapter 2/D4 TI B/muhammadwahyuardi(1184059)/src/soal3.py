# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:34:00 2019

@author: Wahyu
"""

npm = input("masukan npm :")
key = int(npm)%1000
strkey = str(key)
subs = npm[4] + npm[5] + npm[6]

for i in range (int(npm[4])+int(npm[5])+int(npm[6])):
    print("halo",npm[4]+npm[5]+npm[6], "apa kabar?")