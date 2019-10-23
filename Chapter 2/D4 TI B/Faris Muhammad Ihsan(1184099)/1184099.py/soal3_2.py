# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 10:57:57 2019

@author: Faris Fatin 32
"""

npm = input("NPM: ")

val = int(npm[4])
val2 = int(npm[5])
val3 = int(npm[6])

subs = val + val2 + val3
subs2 = val + val2 + val3 

print("Input: "+npm)
print("Output: ")

while subs > 0:
    print("Halo, "+npm[4:7]+" Apa Kabar ?")
    subs = subs - 1
print("..."+str(subs2)+" kali ("+str(val)+"+"+str(val2)+"+"+str(val3)+")...")