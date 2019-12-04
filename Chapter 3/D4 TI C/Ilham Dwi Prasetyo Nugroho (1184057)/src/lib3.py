# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 12:27:13 2019

@author: GL503GE
"""

#fungsi 1
def npm1(npm):
    print(" +++ +++    ++++     +++  +++   ++++++    +++++     ++++++  ")
    print(" +++ +++ +++    +++  +++  +++  +++  +++   ++           ++   ")
    print(" +++ +++    ++++     ++++++++  +++  +++      +++      ++    ")
    print(" +++ +++ +++    +++       +++  +++  +++       ++     ++     ")
    print(" +++ +++    ++++          +++   ++++++    ++++      ++      ")

#fungsi 2
def npm2(npm):
    npm = int (npm)
    abc = abs(npm)%100
    for i in range(abc) :
        print("Hallo, ",npm," apa kabar ")

#fungsi 3
def npm3(npm):
    for i in range(int(str(npm)[4])+int(str(npm)[5])+int(str(npm)[6])):
        print("Hallo, "+str(npm)[4]+str(npm)[5]+str(npm)[6]+" apa kabar ?")
    return None

#fungsi 4 
def npm4(npm):
    key=npm%1000
    str_key=str(key)
    print("Hallo, "+str_key[0]+" apa kabar ?")

#fungsi 5
def npm5(npm):
    a=npm[0]
    b=npm[1]
    c=npm[2]
    d=npm[3]
    e=npm[4]
    f=npm[5]
    g=npm[6]

    for x in a,b,c,d,e,f,g:
        print(x)

#fungsi 6
def npm6(npm):

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
    
#fungsi 7
def npm7(npm):

    a=npm[0]
    b=npm[1]
    c=npm[2]
    d=npm[3]
    e=npm[4]
    f=npm[5]
    g=npm[6]
    conv=1

    for x in a,b,c,d,e,f,g:
        conv*=int(x)
    print(conv)

#fungsi 8
def npm8(npm):
    a=npm[0]
    b=npm[1]
    c=npm[2]
    d=npm[3]
    e=npm[4]
    f=npm[5]
    g=npm[6]
    for x in a,b,c,d,e,f,g:
        if int(x)%2==0:
            if int(x)==0:
                x=""
            print(x,end ="")

#fungsi 9
def npm9(npm):
    a=npm[0]
    b=npm[1]
    c=npm[2]
    d=npm[3]
    e=npm[4]
    f=npm[5]
    g=npm[6]
    for x in a,b,c,d,e,f,g:
    
        if int(x)%2==1:
            print(x,end ="")

#fungsi 10
def npm10(npm):
    a=npm[0]
    b=npm[1]
    c=npm[2]
    d=npm[3]
    e=npm[4]
    f=npm[5]
    g=npm[6]
    for x in a,b,c,d,e,f,g:    
        if int(x) > 1:
            for i in range(2,int(x)):
                if (int(x) % i) == 0:
                    break
            else:
                print(int(x),end =""),