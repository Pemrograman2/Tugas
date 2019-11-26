# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 22:51:33 2019

@author: Azure
"""

def soal6(npm):

    A=npm[0]
    B=npm[1]
    C=npm[2]
    D=npm[3]
    E=npm[4]
    F=npm[5]
    G=npm[6]
    y=0

    for x in A,B,C,D,E,F,G:
        y+=int(x)
    print(y)

i=0
npm=input("Masukan NPM : ")
while i<1:
    if len(npm) < 7:
        print("NPM Kurang dari 7 digit")
        npm=input("Masukan NPM : ")
    elif len(npm) > 7:
        print("NPM lebih dari 7 digit")
        npm=input("Masukan NPM : ")
    else:
        i=1
soal6(npm)