# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 02:11:08 2019

@author: ANIF
"""
#Keterampilan Penanganan Error
def hi(aku):
    try:
        print("Hallo, "+str(aku))
    except:
        print("Terjadi error")
    
hi(input("nama aku: "))
