# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 23:32:48 2019

@author: lovo
"""

def printNPMDuaDijit(npm):
    ulang = 1
    sampai = int(npm[4:3])
    while(ulang <= sampai):
        print("Halo, "+str(npm)+" apa kabar?")
        ulang += 1

printNPMDuaDijit(input("Masukan NPM anda: ")) 