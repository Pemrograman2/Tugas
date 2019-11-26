# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 23:03:35 2019

@author: Azure
"""

import kelas3lib
import lib3


npm=input("Masukan NPM kalian : ")
i=0
while i<1:
    if len(npm) < 7:
        print("NPM Kurang dari 7 digit")
        npm=input("Masukan NPM kalian : ")
    elif len(npm) > 7:
        print("NPM lebih dari 7 digit")
        npm=input("Masukan NPM kalian : ")
    else:
        i=1

#Contoh pemanggilan fungsi pada class
cobakelas=kelas3lib.Kelas3lib(npm) 
hasilkelas=cobakelas.npm1()

print("")

#Contoh pemanggilan fungsi pada library
lib3.npm3(npm)
