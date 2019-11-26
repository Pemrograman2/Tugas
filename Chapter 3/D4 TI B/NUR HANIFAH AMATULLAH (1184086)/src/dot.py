# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:15:28 2019

@author: Lenovo
"""

def pembagian(p,q):
    z=p/q
    return z

a=int(input("angka pertama : "))
b=int(input("angka kedua : "))
try:
    print(pembagian(a,b))
except:
    print("jangan masukan angka 0")
