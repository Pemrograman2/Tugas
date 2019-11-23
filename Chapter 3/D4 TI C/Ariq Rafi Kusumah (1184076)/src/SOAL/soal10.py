# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 00:03:24 2019

@author: Asus
"""

def NPM10(npm):
    
    i=0
    NPM = input("NPM : ")
    while i<1:
        if len(NPM)<7:
            print("NPM kurang dari 7!")
            NPM = input("NPM : ")
        elif len(NPM)>7:
            print("NPM lebih dari 7!")
            NPM = input("NPM : ")
        else:
            i=1
            
    A=NPM[0]
    B=NPM[1]
    C=NPM[2]
    D=NPM[3]
    E=NPM[4]
    F=NPM[5]
    G=NPM[6]
    
    for X in A,B,C,D,E,F,G:    
        if int(X) > 1:
            for i in range(2,int(X)):
                if (int(X) % i) == 0:
                    break
            else:
                print(int(X),end ="")

NPM10(npm)