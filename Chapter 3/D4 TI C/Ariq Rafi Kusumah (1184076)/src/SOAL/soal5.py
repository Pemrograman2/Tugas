# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 23:43:01 2019

@author: Asus
"""

def NPM5(npm):

    i=0
    NPM = input("NPM : ")
    while i<1:
        if len(NPM)<7:
            print("NPM kurang dari 7!")
            NPM = input("Npm : ")
        elif len(NPM)>7:
            print("NPM lebih dari 7!")
            NPM = input("NPM11: ")
        else:
            i=1
            
    A=NPM[0]
    B=NPM[1]
    C=NPM[2]
    D=NPM[3]
    E=NPM[4]
    F=NPM[5]
    G=NPM[6]
    
    for this in A,B,C,D,E,F,G:
        print(this,end = " ")

NPM5(npm)