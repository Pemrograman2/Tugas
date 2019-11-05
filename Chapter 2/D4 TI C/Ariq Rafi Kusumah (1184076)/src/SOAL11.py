# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:42:22 2019

@author: Asus
"""

i=0 
npm=input("Masukkan NPM : ") 
while i <1: 
    if len(npm) <7 : 
        print("NPM kurang dari 7 digit masukkan kembali NPM Anda ! ") 
        npm=input("masukkan NPM : ") 
    elif len(npm) >7 : 
        print("NPM lebih dari 7 digit masukkan kembali NPM Anda ! ") 
        npm=input("masukkan NPM : ") 
    else : 
        i=1 
        a=npm[0] 
        b=npm[1] 
        c=npm[2] 
        d=npm[3] 
        e=npm[4] 
        f=npm[5] 
        g=npm[6] 
        conv=1
for x in a ,b, c ,d, e , f , g : 
    if int (x) > 1: 
        for i in range(2 , int(x )): 
            if ( int(x) % i ) == 0: 
                break 
            else : 
                print( int(x) ,end ="")