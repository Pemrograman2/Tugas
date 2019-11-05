# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 06:59:33 2019

@author: ANIF
"""

#DigitGenap
def printNPMDigitGenap(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 ==0):
          if(n !=0):
              print(n, end = "")
printNPMDigitGenap(input("Masukan NPM anda :"))