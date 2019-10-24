# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 10:40:40 2019

@author: ahmad agung tawakkal
"""

NPM=input("Masukan Npm : ")

X =int(NPM[4])
Y =int(NPM[5])
Z =int(NPM[6])

hitung1 = X + Y + Z
hitung2 = X + Y + Z

while hitung1 > 0:
        print("Halo, ", NPM[4:7], "Apa kabar ?")
        hitung1 = hitung1 -1

print("...",str(hitung2),"hasil dari(",str(X),"+",str(Y),"+"+str(Z),")...")   