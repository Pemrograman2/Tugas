# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 14:37:55 2019

@author: ASUS
"""

npm=int(input("Input1 NPM : "))
key=str(npm%1000)
print("Halo, "+str(npm)[4]+str(npm)[5]+str(npm)[6]+" apa kabar ?")

for i in range(int(str(npm)[4])+int(str(npm)[5])+int(str(npm)[6])-1):
    print("Halo, "+str(npm)[4]+str(npm)[5]+str(npm)[6]+" apa kabar ?")