# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 22:00:55 2019

@author: Asus
"""
class kelas3lib:
    def __init__(npm):
        self.npm = npm
        
    #Jawaban No 1
    def printNPM(npm):
    
        npm = list(str(npm))
    
        angka1 = {"0":" ###### ", "1":"  ##", "2":" ####### ", "3":" ####### ", "4":"     ###", "5":"########", "6":" ####### ", "7":"#########", "8":" ####### ", "9":" #######"}
        angka2 = {"0":"###  ###", "1":"####", "2":"##    ###", "3":"##    ###", "4":"   #####", "5":"##      ", "6":"###      ", "7":"     ### ", "8":"###   ###", "9":"##    ###"}
        angka3 = {"0":"###  ###", "1":" ###", "2":"     ### ", "3":"    #### ", "4":" ###  ##", "5":"####### ", "6":"######## ", "7":"    ###  ", "8":" ### ### ", "9":"##    ###"}
        angka4 = {"0":"###  ###", "1":" ###", "2":"    ###  ", "3":"    #### ", "4":"########", "5":"     ###", "6":"###   ###", "7":"   ###   ", "8":" ### ### ", "9":" ########"}
        angka5 = {"0":"###  ###", "1":" ###", "2":"  ####   ", "3":"##    ###", "4":"     ###", "5":"##   ###", "6":"###   ###", "7":"  ###    ", "8":"###   ###", "9":"      ###"}
        angka6 = {"0":" ###### ", "1":" ###", "2":"#########", "3":" ####### ", "4":"     ###", "5":" ###### ", "6":" ####### ", "7":" ###     ", "8":" ####### ", "9":" ####### "}
              
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


    #Jawaban No 2
    def printNPMDuaDigitBelakang(npm):
        ulang = 1
        sampai = int(npm[5:7])
        while(ulang <= sampai):
            print("Halo, "+str(npm)+" apa kabar?")
            ulang += 1

    printNPMDuaDigitBelakang(input("Masukan NPM anda: "))    

    #Jawaban No 3
    def printNPMTigaDigitBelakang(npm):
        ulang = 1
        sampai = list(map(int, npm[4:7]))
        sampai = sum(sampai)    
        while(ulang <= sampai):
            print("Halo, "+str(npm[-3:])+" apa kabar?")
            ulang += 1
    
    printNPMTigaDigitBelakang(input("Masukan NPM anda: "))

    #Jawaban No 4
    def printNPMDigitKetigaBelakang(npm):
        print("Output:")
        print("Halo, " + str(npm[-3]) + " Apa Kabar?")
             
    printNPMDigitKetigaBelakang(input("Input :"))

    #Jawaban No 5
    def printNPMSatuSatu(npm):
        npm = (list(map(int, npm)))
        for n in npm:
            print (n)
        
    printNPMSatuSatu(input ("Masukkan NPM kamu :"))

    #Jawaban No 6
    def printNPMPenjumlahan(npm):
        npm = list(map(int, npm))
        hasil = 0
        for x in npm:
            hasil += x
    
        print(hasil)
    
    printNPMPenjumlahan(input("Masukan NPM anda: "))

    #Jawaban No 7
    def printNPMPerkalian(npm):
        npm = list(map(int, npm))
        hasil = 0
        for x in npm:
            hasil *= x
    
        print(hasil)
    
    printNPMPerkalian(input("Masukan NPM anda: "))

    #Jawaban No 8
    def printNPMGenap(npm):
        npm = list(map(int, npm))
        for n in npm:
            if(n % 2 == 0):
                if(n != 0):
                    print(n, end = "")
    
    printNPMGenap(input("Masukan NPM anda: "))

    #Jawaban No 9
    def printNPMGanjil(npm):
        npm = list(map(int, npm))
        for n in npm:
            if(n % 2 != 0):
                print(n, end = "")
    
    printNPMGanjil(input("Masukan NPM anda: "))

    #Jawaban No 10
    def printNPMPrima(npm):
        npm = list(map(int, npm))
        prima = []
        for n in npm:
            isPrime = True
            if n == 0 or n == 1:
                isPrime = False
                for x in range (2,n):
                    if n % x == 0:
                        isPrime = False
                        if isPrime:
                            prima.append(n)
            
        for p in prima:
            print(p, end = "")
    
    printNPMPrima(input("Masukan NPM anda: "))