# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 14:40:15 2019

@author: ASUS
"""

i=0
npm=input("Input NPM : ")
while i<1:
    if len(npm) < 7:
        print("NPM Kurang dari 7 digit")
        npm=input("Input NPM : ")
    elif len(npm) > 7:
        print("NPM lebih dari 7 digit")
        npm=input("Input NPM : ")
    else:
        i=1
a=npm[0]
b=npm[1]
c=npm[2]
d=npm[3]
e=npm[4]
f=npm[5]
g=npm[6]
conv=1

for x in a,b,c,d,e,f,g:
    
    if int(x)%2==0:
        if int(x)==0:
            x=""
        print(x,end ="")