# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:49:59 2019

@author: trian
"""
var_str = "10"
var_int = 10

try:
    jumlah = var_str + var_int
    print(jumlah)
except:
    print("String tidak bisa ditambahkan dengan Integer!")
    print("Tolong perbaiki tipe data string, konversikan terlebih dahulu ke integer.")