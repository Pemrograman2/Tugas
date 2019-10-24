# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 07:25:31 2019

@author: Hanif Amrullah
"""

npm = "1184020"

a=npm[0]
b=npm[1]
c=npm[2]
d=npm[3]
e=npm[4]
f=npm[5]
g=npm[6]

for x in a,b,c,d,e,f,g, :
    if int(x)%2==1:
        for i in range(2,int(x)):
            if (int(x)%i) == 0:
                break
        else :
            print(int(x),end =""),