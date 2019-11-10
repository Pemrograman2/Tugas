# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 06:24:46 2019

@author: User
"""
def perulangan():
    while hitungan > 0:
        print("Haiii, ", NPM[4:7], "Apa kabar ?")
        hitungan = hitungan -1
        print("...",str(hitungan),"kali(",str(A),"+",str(B),"+"+str(C),")...")  

NPM=input("berapa npm kamu? ")

A =int(NPM[4])
B =int(NPM[5])
C =int(NPM[6])

hitungan = A + B + C
hitungan2 = A + B + C

perulangan()