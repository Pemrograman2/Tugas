# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:16:19 2019

@author: ahmad agung tawakkal
"""
#fungsi 1
def NPM1(npm):
    print(" *** ***     ****     ***  ***   ******   ***  ******** ")
    print(" *** ***  ***    ***  ***  ***  ***  ***  ***  ******** ")
    print(" *** ***  ***    ***  ***  ***  ***  ***  ***  ***      ")
    print(" *** ***     ****     ********  ***  ***  ***  ******** ")
    print(" *** ***     ****     ********  ***  ***  ***  ******** ")
    print(" *** ***  ***    ***       ***  ***  ***  ***       *** ")
    print(" *** ***  ***    ***       ***  ***  ***  ***  ******** ")
    print(" *** ***     ****          ***   ******   ***  ******** ") 

#fungsi 2    
def NPM2(npm):
    npm = int (npm)
    Tld=abs(npm)%100
    for i in range(Tld):
        print ("Hallo, ",npm," apa kabar ?")
        
#fungsi 3
def NPM3(npm):
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
        
#fungsi 4
def NPM4(npm):
    NPM = input ("Masukan NPM : ")
    print ("Halo, ",NPM[4]," apa kabar ?")
    
#fungsi 5
def NPM5(npm):

    i=0
    NPM = input("NPM : ")
    while i<1:
        if len(NPM)<7:
            print("NPM kurang dari 7!")
            NPM = input("Npm : ")
        elif len(NPM)>7:
            print("NPM lebih dari 7!")
            NPM = input("NPM11: ")
        else:
            i=1
            
    A=NPM[0]
    B=NPM[1]
    C=NPM[2]
    D=NPM[3]
    E=NPM[4]
    F=NPM[5]
    G=NPM[6]
    
    for this in A,B,C,D,E,F,G:
        print(this,end = " ")
        
#fungsi 6
def NPM6(npm):

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
    
    X=0
    
    for this in A,B,C,D,E,F,G:
       X+=int(this)
    print(X)   
    
#fungsi 7
def NPM7(npm):
    
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
    
    X=1
    
    for this in A,B,C,D,E,F,G:
        X*=int(this)
    print(X)
    
#fungsi 8
def NPM8(npm):
    
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
    
    X=1
    
    for this in A,B,C,D,E,F,G:
       
        if int(this)%2==0:
            if int(this)==0:
                this=""
            print(this,end =" ")
            
#fungsi 9
def NPM9(npm):
    
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
    
    X=1
    
    for this in A,B,C,D,E,F,G:
        
        if int(this)%2==1:
            print(this,end=" ")   

#fungsi 10
def NPM10(npm):
    
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