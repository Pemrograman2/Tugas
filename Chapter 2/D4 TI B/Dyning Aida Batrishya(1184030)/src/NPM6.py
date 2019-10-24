# -*- coding: utf-8 -*-
"""

@author: ASS
"""

i=0
NPM = input("Npm kamu adalah : ")
while i<1:
    if len(NPM)<7:
        print("Npm kurang dari digit")
        NPM = input("Npm kamu: ")
    elif len(NPM)>7:
        print("Npm lebih dari 7 digit")
        NPM = input("Npm kamu: ")
    else:
        i=1
        
A=NPM[0]
B=NPM[1]
C=NPM[2]
D=NPM[3]
E=NPM[4]
F=NPM[5]
G=NPM[6]

X=0

for this in A,B,C,D,E,F,G:
   X+=int(this)
print(X)   
        