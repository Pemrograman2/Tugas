# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:34:55 2019

@author: ahmad agung tawakkal
"""

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

