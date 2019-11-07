# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 03:45:12 2019

@author: acer
"""

def x(npm):

    a  = 1
    b = list(map(int, npm[4:7]))
    b = sum(b)     
    while(a <= b):
        print("Halo, "+str(npm[-3:])+" apa kabar?") 
        a += 1

x(input("Masukkan NPM Anda: "))