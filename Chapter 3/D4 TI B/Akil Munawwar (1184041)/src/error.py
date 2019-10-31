# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 22:17:29 2019

@author: Asus
"""

def itung(angka):
    try:
        print("Ini angka "+int(angka))
    except:
        print("Bukan angka") 

itung(input("Masukan angka anda: "))