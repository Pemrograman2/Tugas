# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 00:03:10 2019

@author: lovo
"""

def printNPMDijitPrima(npm):
    npm = list(map(int, npm))
    prima = []
    for n in npm:
        isPrime = True
        if n == 0 or n == 1:
            isPrime = False
        for x in range(2, n):
            if n % x == 0:
                isPrime = False
        if isPrime:
            prima.append(n)

    for p in prima:
        print(p, end = "")

printNPMDijitPrima(input("Masukan NPM anda: "))