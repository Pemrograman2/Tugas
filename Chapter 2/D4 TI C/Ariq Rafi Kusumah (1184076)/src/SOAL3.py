# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 14:32:54 2019

@author: Asus
"""

npm = input("masukan npm : ") 
key = int(npm)%1000 
strkey = str (key) 
subs = npm[4] + npm[5] + npm[6]

for i in range ( int(npm[4])+ int(npm[5])+ int(npm[ 6 ] ) ) : 
    print("halo" ,npm[4]+npm[5]+npm[6] , "apa kabar?") 