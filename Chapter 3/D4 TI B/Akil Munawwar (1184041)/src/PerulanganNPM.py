# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 20:58:28 2019

@author: Asus
"""

def printNPMDuaDigitBelakang(npm):
    ulang = 1
    sampai = int(npm[5:7])
    while(ulang <= sampai):
        print("Halo, "+str(npm)+" apa kabar?")
        ulang += 1

printNPMDuaDigitBelakang(input("Masukan NPM anda: "))    