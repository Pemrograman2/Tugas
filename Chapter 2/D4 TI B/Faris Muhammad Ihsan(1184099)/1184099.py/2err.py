# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 21:31:38 2019

@author: Faris Fatin 32
"""

var1 = input("Variable String: ")
var2 = input("Variable Integer: ")

string = str(var1)
integer = int(var2)
try:
    jml = string+integer
except Exception:
    print("gagal euy")