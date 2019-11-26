# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 23:00:48 2019

@author: Azure
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
