# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 23:50:14 2019

@author: lovo
"""

def printNPMTigaDijit(npm):
    ulang = 1
    sampai = list(map(int, npm[0:3]))
    sampai = sum(sampai)    
    while(ulang <= sampai):
        print("Halo, "+str(npm[-3:])+" apa kabar?")
        ulang += 1

printNPMTigaDijit(input("Masukan NPM anda: "))