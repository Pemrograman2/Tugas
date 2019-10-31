# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 11:59:04 2019

@author: Hanif Amrullah
"""

def pembagian(a,b):
    c=a/b
    return c

d=int(input("angka pertama : "))
e=int(input("angka kedua : "))
try:
    print(pembagian(d,e))
except:
    print("jangan masukan angka 0")