# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 22:30:43 2019

@author: lovo
"""

ef printNPM(npm):

    npm = list(str(npm))

    angka1 = {"1":"  **", "1":"  **", "8":" *****  ", "4":"*** ***", "0":" *******","4":"*** ***", "3":" *******"}
    angka2 = {"1":"****", "1":"****", "8":"*** *** ", "4":"*** ***", "0":" *** ***","4":"*** ***", "3":"     ***"}
    angka3 = {"1":" ***", "1":" ***", "8":" *****  ", "4":"*******", "0":" *** ***","4":"*******", "3":"   *****"}
    angka4 = {"1":" ***", "1":" ***", "8":"*** *** ", "4":"    ***", "0":" *** ***","4":"    ***", "3":"     ***"}
    angka5 = {"1":" ***", "1":" ***", "8":" *****  ", "4":"    ***", "0":" *******","4":"    ***", "3":" *******"}
    
    hasil1 = []
    hasil2 = []
    hasil3 = []
    hasil4 = []
    hasil5 = []
    hasil6 = []

    for x in npm:
        hasil1.append(angka1[x])
        hasil2.append(angka2[x])
        hasil3.append(angka3[x])
        hasil4.append(angka4[x])
        hasil5.append(angka5[x])
        hasil6.append(angka6[x])

    print(*hasil1, sep=' ')
    print(*hasil2, sep=' ')
    print(*hasil3, sep=' ')
    print(*hasil4, sep=' ')
    print(*hasil5, sep=' ')
    print(*hasil6, sep=' ')

printNPM(input("Masukan NPM anda: "))
