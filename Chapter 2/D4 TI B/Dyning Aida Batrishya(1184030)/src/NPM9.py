# -*- coding: utf-8 -*-
"""

@author: ASS
"""

i=0
NPM = input("berapa npm kamu : ")
while i<1:
    if len(NPM)<7:
        print("Npmnya kurang dari 7 digit")
        NPM = input("Npm kamu : ")
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

X=1

for this in A,B,C,D,E,F,G:
   
    if int(this)%2==0:
        if int(this)==0:
            this=""
        print(this,end =" ")    
        