# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 15:09:10 2019

@author: trian
"""
#Modulus
print("Soal no 1")

print("Masukkan NPM anda: ")
NPM = input()

npm = int(NPM) % 3
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

#Hello NPM
print("Soal No 2")

Loop = NPM[5:7]

for x in range(int(Loop)):
    print("Hallo " + NPM + " Apa Kabar?")

#3 digit belakang NPM
print("Soal No 2")

Loop = NPM[4:7]

total = int(NPM[5]) + int(NPM[6])

for x in range(total):
    print("Hallo " + Loop + " Apa Kabar?")

#digit ke 3
print("Soal No 3")

Loop = NPM[4]
print("Hello " + Loop + " Apa Kabar?")

#variabel alfabet
print("Soal no 5")

var = "abcdefg"
index = 0

for i in var:
    print(i + " = " + NPM[index])
    index += 1

#penjumlahan NPM  
print("Soal no 6")

index = 0
angka = 0

for i in NPM:
    jumlah = int(NPM[index]) + int(angka)
    angka = jumlah
    index += 1
    
print(jumlah)

#perkalian NPM
print("Soal no 7")

index = 0
angka = 0

for i in NPM:
    jumlah = int(NPM[index]) * int(angka)
    angka = jumlah
    index += 1
    
print(jumlah)

#print vertical
print("Soal no 8")

for i in NPM:
    print(i)

#digit genap NPM
print("Soal no 9")

index = 0
for i in NPM:
    if (int(NPM[index])%2 == 0) & (int(NPM[index]) != 0):
        print(NPM[index])
    index += 1
    
#digit ganjil NPM
print("Soal no 10")

index = 0
for i in NPM:
    if (int(NPM[index])%2 != 0) & (int(NPM[index]) != 0):
        print(NPM[index])
    index += 1
  
#bilangan prima NPM
print("Soal no 11") 
index = 0  
 
for i in NPM:
    prima = True
    var=int(NPM[index])
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







    

    


    