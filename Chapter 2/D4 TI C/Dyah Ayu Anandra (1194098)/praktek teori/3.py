# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 22:11:30 2019

@author: Dell
"""

npm=int(input("Input1 NPM : "))
key=str(npm%1000)
print("Hallo, "+str(npm)[4]+str(npm)[5]+str(npm)[6]+" apa kabar ?")

for i in range(int(str(npm)[4])+int(str(npm)[5])+int(str(npm)[6])-1):
    print("Hallo, "+str(npm)[4]+str(npm)[5]+str(npm)[6]+" apa kabar ?")