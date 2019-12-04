# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 03:09:37 2019

@author: Aditya Luthfi
"""

def npm8(npm):
    
    a=npm[0]
    b=npm[1]
    c=npm[2]
    d=npm[3]
    e=npm[4]
    f=npm[5]
    g=npm[6]
    conv=1
    
    for x in a, b, c, d, e, f, g:
        if int(x)%2==0:
            if int(x)==0:
                x=""
            print(x, end ="")
            
i=0
npm=input("Masukkan NPM : ")
while i<1:
    if len(npm) < 7:
        print ("NPM Kurang dari 7 digit")
        npm=input("Masukkan NPM : ")
    elif len(npm) > 7:
         print ("NPM lebih dari 7 digit")
         npm=input("Masukkan NPM : ")
    else:
        i=1
npm8(npm)