# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 11:57:19 2019

@author: Aditya Luthfi
"""

def npm1(npm):
    print("+++ +++  +++++  +++ +++ +++++++ +++++++ +++++++")
    print("+++ +++ +++ +++ +++ +++ +++ +++ +++ +++ +++ +++")
    print("+++ +++  +++++  +++++++ +++ +++ +++++++ +++ +++")
    print("+++ +++ +++ +++     +++ +++ +++     +++ +++ +++")
    print("+++ +++  +++++      +++ +++++++ +++++++ +++++++")
    
def npm2(npm):
    npm = input("masukan npm : ") 
    key = int(npm)%100
    for i in range(key): 
        print("Halo" ,npm, "Apa Kabar?")
        
def npm3(npm):
    for i in range(int (str(npm)[4]) + int (str(npm)[5]) + int (str(npm)[6])):
        print ("Halo, " + str(npm)[4] + str(npm)[5] + str(npm)[6] + " apa kabar ?")
        
i = 0
npm = input ("Masukan NPM : ")
while i < 1:
    if len (npm) < 7:
        print ("NPM Kurang dari 7 digit")
        npm = input ("Masukan NPM : ")
    elif len (npm) > 7:
        print ("NPM lebih dari 7 digit")
        npm = input ("Masukan NPM : ")
    else :
        i = 1
        
def npm4(npm):
  npm = input ("Masukkan NPM : ")
  print ("Halo, ", npm[4], "apa kabar ? ")


def npm5(npm):
    a=npm[0]
    b=npm[1]
    c=npm[2]
    d=npm[3]
    e=npm[4]
    f=npm[5]
    g=npm[6]
    
    for x in a, b, c, d, e, f, g:
        print(x)
        
i=0
npm=input("Masukkan NPM : ")
while i <1:
    if len(npm) < 7:
        print ("NPM Kurang dari 7 digit")
        npm=input("Masukkan NPM : ")
    elif len(npm) > 7:
         print ("NPM lebih dari 7 digit")
         npm=input("Masukkan NPM : ")
    else:
        i=1
        
        
def npm6(npm):
    
    a=npm[0]
    b=npm[1]
    c=npm[2]
    d=npm[3]
    e=npm[4]
    f=npm[5]
    g=npm[6]
    y=0
    
    for x in a, b, c, d, e, f, g:
        y+=int(x)
    print(y)
    
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
        
        
def npm7(npm):
    
    a=npm[0]
    b=npm[1]
    c=npm[2]
    d=npm[3]
    e=npm[4]
    f=npm[5]
    g=npm[6]
    conv=1
    
    for x in a, b, c, d, e, f, g:
        conv*=int(x)
    print(conv)
    
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
        
        
def npm9(npm):
    
    a=npm[0]
    b=npm[1]
    c=npm[2]
    d=npm[3]
    e=npm[4]
    f=npm[5]
    g=npm[6]
    
    for x in a, b, c, d, e, f, g:
        
        if int(x)%2==1:
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
        
        
def npm10(npm):
    
    a=npm[0]
    b=npm[1]
    c=npm[2]
    d=npm[3]
    e=npm[4]
    f=npm[5]
    g=npm[6]
    
    for x in a, b, c, d, e, f, g:
        if int(x) > 1:
            for i in range(2, int(x)):
                if (int(x) % i)==0:
                    break
                else:
                    print(int(x) ,end ="")
                    
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