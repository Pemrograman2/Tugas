# -*- coding: utf-8 -*-
"""
@author: ASS
"""

NPM=input("berapa npm kamu? ")

A =int(NPM[4])
B =int(NPM[5])
C =int(NPM[6])

hitung1 = A + B + C
hitung2 = A + B + C

while hitung1 > 0:
        print("Halo, ", NPM[4:7], "Apa kabar ?")
        hitung1 = hitung1 -1
print("...",str(hitung2),"kali(",str(A),"+",str(B),"+"+str(C),")...")   