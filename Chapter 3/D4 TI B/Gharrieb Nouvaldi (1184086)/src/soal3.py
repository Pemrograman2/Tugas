# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 22:35:04 2019

@author: Azure
"""

def soal3(npm):
    for i in range(int(str(npm)[4])+int(str(npm)[5])+int(str(npm)[6])):
        print("Halo, "+str(npm)[4]+str(npm)[5]+str(npm)[6]+" apa kabar ?")

i=0
npm=input("Masukan Npm : ")
while i<1:
    if len(npm) < 7:
        print("Npm Kurang dari 7 digit")
        npm=input("Masukan Npm : ")
    elif len(npm) > 7:
        print("NPM lebih dari 7 digit")
        npm=input("Masukan Npm : ")
    else:
        i=1
soal3(npm)