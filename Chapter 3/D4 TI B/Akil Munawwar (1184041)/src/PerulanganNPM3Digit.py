# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 21:03:27 2019

@author: Asus
"""

def printNPMTigaDigitBelakang(npm):
    ulang = 1
    sampai = list(map(int, npm[4:7]))
    sampai = sum(sampai)    
    while(ulang <= sampai):
        print("Halo, "+str(npm[-3:])+" apa kabar?")
        ulang += 1
    
printNPMTigaDigitBelakang(input("Masukan NPM anda: "))