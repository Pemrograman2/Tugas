# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 10:47:43 2019

@author: Lenovo
"""

#soal1
def soal1():
    print("### ###  ######    ###   ###    ######       ######    #######")
    print("### ### ###   ###  ###   ###  ###     ###  ###    ###  ##     ")
    print("### ###  ######    #########  ###     ###    ######    #######")
    print("### ### ###   ###        ###  ###     ###  ###    ###  ##   ##")
    print("### ###  ######          ###    ######       ######    #######")         
          
#soal2
def soal2(npm):
    npm=int(npm)
    TwoLastDigit=abs(npm)%100
    for i in range(TwoLastDigit):
       print("Halo, ", npm, " apa kabar ?")
       
#soal3
def soal3(npm):
    npm=int(input("Masukan NPM : "))
    key=str(npm%1000)
    print("Halo, "+str(npm)[4]+str(npm)[5]+str(npm)[6]+" apa kabar ?")
    
     for i in range(int(str(npm)[4])+int(str(npm)[5])+int(str(npm)[6])-1):
        print("Halo, "+str(npm)[4]+str(npm)[5]+str(npm)[6]+" apa kabar ?")

#soal4    
def soal4(npm):
    npm=input("Masukan NPM : "))
    key=npm%1000
    str_key=str(key)
    print("Halo, "+str_key[0]+" apa kabar ?")

#soal5
def soal5(npm):
    i=0
npm=input("Masukan NPM : ")
while i<1:
    if len(npm) < 7:
        print("NPM Kurang dari 7 digit")
        npm=input("Masukan NPM : ")
    elif len(npm) > 7:
        print("NPM lebih dari 7 digit")
        npm=input("Masukan NPM : ")
    else:
        i=1
        
    A=npm[0]
    B=npm[1]
    C=npm[2]
    D=npm[3]
    E=npm[4]
    F=npm[5]
    G=npm[6]

    for x in A,B,C,D,E,F,G:
        print(x)
        
#soal6
def soal6(npm):
    i=0
npm=input("Masukan NPM : ")
while i<1:
    if len(npm) < 7:
        print("NPM Kurang dari 7 digit")
        npm=input("Masukan NPM : ")
    elif len(npm) > 7:
        print("NPM lebih dari 7 digit")
        npm=input("Masukan NPM : ")
    else:
        i=1

    A=npm[0]
    B=npm[1]
    C=npm[2]
    D=npm[3]
    E=npm[4]
    F=npm[5]
    G=npm[6]
    y=0

    for x in A,B,C,D,E,F,G:
        y+=int(x)
    print(y)

#soal7
def soal6(npm):
    i=0
npm=input("Masukan NPM : ")
while i<1:
    if len(npm) < 7:
        print("NPM Kurang dari 7 digit")
        npm=input("Masukan NPM : ")
    elif len(npm) > 7:
        print("NPM lebih dari 7 digit")
        npm=input("Masukan NPM : ")
    else:
        i=1

    A=npm[0]
    B=npm[1]
    C=npm[2]
    D=npm[3]
    E=npm[4]
    F=npm[5]
    G=npm[6]
    conv=1
    
    for x in a,b,c,d,e,f,g:
        conv*=int(x)
    print(conv)
    
#soal8
def soal8(npm):
    i=0
npm=input("Masukan NPM : ")
while i<1:
    if len(npm) < 7:
        print("NPM Kurang dari 7 digit")
        npm=input("Masukan NPM : ")
    elif len(npm) > 7:
        print("NPM lebih dari 7 digit")
        npm=input("Masukan NPM : ")
    else:
        i=1
        
    A=npm[0]
    B=npm[1]
    C=npm[2]
    D=npm[3]
    E=npm[4]
    F=npm[5]
    G=npm[6]
    conv=1

    for x in A,B,C,D,E,F,G:
       if int(x)%2==0:
            if int(x)==0:
                x=""
            print(x,end ="")
#soal9
def soal9(npm):
    i=0
npm=input("Masukan NPM : ")
while i<1:
    if len(npm) < 7:
        print("NPM Kurang dari 7 digit")
        npm=input("Masukan NPM : ")
    elif len(npm) > 7:
        print("NPM lebih dari 7 digit")
        npm=input("Masukan NPM : ")
    else:
        i=1
        
    A=npm[0]
    B=npm[1]
    C=npm[2]
    D=npm[3]
    E=npm[4]
    F=npm[5]
    G=npm[6]
    conv=1

    for x in A,B,C,D,E,F,G:
    
        
        if int(x)%2==1:
            print(x,end ="")
#soal10
def soal10(npm):
    i=0
npm=input("Masukan NPM : ")
while i<1:
    if len(npm) < 7:
        print("NPM Kurang dari 7 digit")
        npm=input("Masukan NPM : ")
    elif len(npm) > 7:
        print("NPM lebih dari 7 digit")
        npm=input("Masukan NPM : ")
    else:
        i=1
        
    A=npm[0]
    B=npm[1]
    C=npm[2]
    D=npm[3]
    E=npm[4]
    F=npm[5]
    G=npm[6]
   conv=1

    for x in a,b,c,d,e,f,g:    
        if int(x) > 1:
            for i in range(2,int(x)):
                if (int(x) % i) == 0:
                    break
            else:
                print(int(x),end =""),


