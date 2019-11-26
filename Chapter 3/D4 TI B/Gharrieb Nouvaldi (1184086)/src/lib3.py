# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 22:58:41 2019

@author: Azure
"""

def soal1():
    print("### ###  ######    ###   ###    ######       ######    #######")
    print("### ### ###   ###  ###   ###  ###     ###  ###    ###       ##")
    print("### ###  ######    #########  ###     ###    ######    #######")
    print("### ### ###   ###        ###  ###     ###  ###    ###  ##     ")
    print("### ###  ######          ###    ######       ######    #######")         
          
def soal2(npm):
    npm=int(npm)
    TwoLastDigit=abs(npm)%100
    for i in range(TwoLastDigit):
       print("Halo, ", npm, " apa kabar ?")
       
def soal3(npm):
    for i in range(int(str(npm)[4])+int(str(npm)[5])+int(str(npm)[6])):
        print("Halo, "+str(npm)[4]+str(npm)[5]+str(npm)[6]+" apa kabar ?")
    return None

def soal4(npm):
    key=npm%1000
    str_key=str(key)
    print("Halo, "+str_key[0]+" apa kabar ?")

def soal5(npm):
    A=npm[0]
    B=npm[1]
    C=npm[2]
    D=npm[3]
    E=npm[4]
    F=npm[5]
    G=npm[6]

    for x in A,B,C,D,E,F,G:
        print(x)

def soal6(npm):

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

def soal7(npm):

    A=npm[0]
    B=npm[1]
    C=npm[2]
    D=npm[3]
    E=npm[4]
    F=npm[5]
    G=npm[6]
    conv=1

    for x in A,B,C,D,E,F,G:
        conv*=int(x)
    print(conv)

def soal8(npm):
    A=npm[0]
    B=npm[1]
    C=npm[2]
    D=npm[3]
    E=npm[4]
    F=npm[5]
    G=npm[6]
    for x in A,B,C,D,E,F,G:
        if int(x)%2==0:
            if int(x)==0:
                x=""
            print(x,end ="")

def soal9(npm):
    A=npm[0]
    B=npm[1]
    C=npm[2]
    D=npm[3]
    E=npm[4]
    F=npm[5]
    G=npm[6]
    for x in A,B,C,D,E,F,G:
    
        if int(x)%2==1:
            print(x,end ="")

def soal10(npm):
    A=npm[0]
    B=npm[1]
    C=npm[2]
    D=npm[3]
    E=npm[4]
    F=npm[5]
    G=npm[6]
    for x in A,B,C,D,E,F,G:    
        if int(x) > 1:
            for i in range(2,int(x)):
                if (int(x) % i) == 0:
                    break
            else:
                print(int(x),end =""),
