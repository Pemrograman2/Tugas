# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 22:34:29 2019

@author: ASUS
"""

def listsatupersatu(npm):
    npm = list(map(int, npm))  
    for n in npm:
        print(n)

listsatupersatu(input("NPM: "))