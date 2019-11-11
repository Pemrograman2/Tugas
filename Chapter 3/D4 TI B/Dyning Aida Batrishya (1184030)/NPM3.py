# -*- coding: utf-8 -*-
"""
@author: ASS
"""
def hello_world(npm):
        for x in range(int(str(npm)[4])+int(str(npm)[5])+int(str(npm)[6])):
                print("Halo, "+str(npm)[4]+str(npm)[5]+str(npm)[6]+" Apa kabar?")

x=0
npm = input("Berapa npm kamu?")
while x<1:
        if len(npm) < 7:
                print("NPM kamu kurang dari 7 digit")
                npm = input("Lalu Berapa npm kamu?")
        elif len(npm) > 7:
                print("NPM kamu lebih dari 7 digit")7-=
                npm = input("Lalu Berapa npm kamu?")
        else:
                x=1

hello_world(npm)