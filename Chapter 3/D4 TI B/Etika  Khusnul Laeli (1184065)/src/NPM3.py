# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 06:24:46 2019

@author: ANIF
"""

def printNPMTigaDigit(npm):

    ulang  = 1
    sampai = list(map(int, npm[3:7]))
    sampai = sum(sampai)     
    while(ulang <= sampai):
        print("Halo, "+str(npm[-3:])+" apa kabar?") 
        ulang += 1

printNPMTigaDigit(input("Masukkan NPM Anda: "))