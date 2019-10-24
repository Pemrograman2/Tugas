# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 22:19:12 2019

@author: lenovo
"""

npm=int(input("Masukan NPM : "))
key=str(npm%1000)
print("Hallo, "+str(npm)[4]+str(npm)[5]+str(npm)[6]+" Apa kabar?")

for i in range(int(str(npm)[4])+int(str(npm)[5])+int(str(npm)[6])-1):
         print("Hallo, "+str(npm)[4]+str(npm)[5]+str(npm)[6]+" Apa kabar?")