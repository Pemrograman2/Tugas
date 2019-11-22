# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:09:10 2019

@author: trian
"""
class Kelas:
    def __init__(self, NPM):
        self.NPM = NPM
    
    def Modulus(self):
        #Modulus
        print("Soal no 1")
        
        npm = int(self.NPM) % 3
        print(npm)
        
        print("###   ###   #########   ###   ###   #########   ###   ###")
        print("###   ###   #########   ###   ###   #########   ###   ###")
        print("###   ###   ###   ###   ###   ###   ###   ###   ###   ###")
        print("###   ###   ###   ###   ###   ###   ###   ###   ###   ###")
        print("###   ###   #########   #########   ###   ###   ###   ###")
        print("###   ###   ###   ###         ###   ###   ###   ###   ###")
        print("###   ###   ###   ###         ###   ###   ###   ###   ###")
        print("###   ###   #########         ###   #########   ###   ###")
        print("###   ###   #########         ###   #########   ###   ###")

    def Hello_NPM(self):
        #Hello NPM
        print("Soal No 2")
        
        Loop = self.NPM[5:7]
        
        for x in range(int(Loop)):
            print("Hallo " + self.NPM + " Apa Kabar?")

    def NPM_DigitBelakang(self):
        #3 digit belakang NPM
        print("Soal No 3")
        
        Loop = self.NPM[4:7]
        
        total = int(self.NPM[5]) + int(self.NPM[6])
        
        for x in range(total):
            print("Hallo " + Loop + " Apa Kabar?")

    def NPM_DigitKetiga(self):
        #digit ke 3
        print("Soal No 4")
        
        Loop = self.NPM[4]
        print("Hello " + Loop + " Apa Kabar?")
    
    def Variabel_Alfabet(self):
        #variabel alfabet
        print("Soal no 5")
        
        var = "abcdefg"
        index = 0
        
        for i in var:
            print(i + " = " + self.NPM[index])
            index += 1
            
    def Penjumlahan_NPM(self):
        #penjumlahan NPM  
        print("Soal no 6")
        
        index = 0
        angka = 0
        
        for i in self.NPM:
            jumlah = int(self.NPM[index]) + int(angka)
            angka = jumlah
            index += 1
            
        print(jumlah)
        
    def Perkalian_NPM(self):
        #perkalian NPM
        print("Soal no 7")
        
        index = 0
        angka = 0
        
        for i in self.NPM:
            jumlah = int(self.NPM[index]) * int(angka)
            angka = jumlah
            index += 1
            
        print(jumlah)
        
    def Print_Vertical(self):
        #print vertical
        print("Soal no 8")
        
        for i in self.NPM:
            print(i)
            
    def DigitGenap(self):
        #digit genap NPM
        print("Soal no 9")
        
        index = 0
        for i in self.NPM:
            if (int(self.NPM[index])%2 == 0) & (int(self.NPM[index]) != 0):
                print(self.NPM[index])
            index += 1
            
    def DigitGanjil(self):
        #digit ganjil NPM
        print("Soal no 10")
        
        index = 0
        for i in self.NPM:
            if (int(self.NPM[index])%2 != 0) & (int(self.NPM[index]) != 0):
                print(self.NPM[index])
            index += 1
            
    def PrimaNPM(self):
        #bilangan prima NPM
        print("Soal no 11") 
        index = 0  
         
        for i in self.NPM:
            prima = True
            var=int(self.NPM[index])
            if(var<=1):
                prima=False
            for i in range (2,var):
                if(var%i==0):
                    prima=False
            if(prima==True):
                print(var,"Prima")
            else:
                print(var,"bukan prima")
            index += 1







    

    


    