# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 23:46:35 2019

@author: Dell
"""

i=0
npm=input("input NPM : ")
while i<1:
    if len(npm) < 7:
        print("NPM Kurang dari 7 digit")
        npm=input("input NPM : ")
    elif len(npm) > 7:
        print("NPM lebih dari 7 digit")
        npm=input("input NPM : ")
    else:
        i=1
a=npm[0]
b=npm[1]
c=npm[2]
d=npm[3]
e=npm[4]
f=npm[5]
g=npm[6]
y=0

for x in a,b,c,d,e,f,g:
    y+=int(x)
print(y)