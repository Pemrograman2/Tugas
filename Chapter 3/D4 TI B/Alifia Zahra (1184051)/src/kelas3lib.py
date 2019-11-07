class kelas3lib:
    def __init__(self, npm):
        self.npm = npm
        
#SOAL1
        
def printNPM(npm):
 
    npm = list(str(npm))
 
    angka1 = {"0":" ###### ", "1":"  ##", "2":" ###### ", "3":"####### ", "4":"    ###",  "5":"######## ", "6":" #######", "7":"#########", "8":" ####### "}
    angka2 = {"0":"###  ###", "1":"####", "2":"##   ###", "3":"##   ###", "4":"  #####",  "5":"##       ", "6":"###     ", "7":"      ###", "8":"###   ###"}
    angka3 = {"0":"###  ###", "1":" ###", "2":"    ### ", "3":"   ###  ", "4":" ### ##",  "5":"######## ", "6":"########", "7":"     ### ", "8":"  #####  "}
    angka4 = {"0":"###  ###", "1":" ###", "2":"   ###  ", "3":"   ###  ", "4":"#######",  "5":"      ###", "6":"###  ###", "7":"    ###  ", "8":"  #####  "}
    angka5 = {"0":"###  ###", "1":" ###", "2":"  ###   ", "3":"##   ###", "4":"    ###",  "5":"##    ###", "6":"###  ###", "7":"   ###   ", "8":"###   ###"}
    angka6 = {"0":" ###### ", "1":" ###", "2":"########", "3":"####### ", "4":"    ###",  "5":" ######  ", "6":"########", "7":"  ###    ", "8":" ####### "}

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

#SOAL2
def perulangan(npm):
    hitung = 0
    while(hitung < 65):
        print("Hallo, 1184065 apa kabar")
    hitung = hitung + 1
    
perulangan(int(input("Masukan NPM: ")))

#SOAL3
def printNPMTigaDigit(npm):

    ulang  = 1
    sampai = list(map(int, npm[3:7]))
    sampai = sum(sampai)     
    while(ulang <= sampai):
        print("Halo, "+str(npm[-3:])+" apa kabar?") 
        ulang += 1

printNPMTigaDigit(input("Masukkan NPM Anda: "))

#SOAL4
def printdigit_ketiga(npm):

    print("Output:") 
    print("Halo, "+str(npm[-3])+" apa kabar?")

printdigit_ketiga(input("Masukkan NPM Anda:"))

#SOAL5
def satupersatu(npm):

    npm = list(map(int, npm))  
    for n in npm:
        print(n)

satupersatu(input("Masukkan NPM Anda: "))

#SOAL6
def printpenjumlahan(npm):

    npm = list(map(int, npm))
    hasil = 0
    for n in npm:
        hasil += n 
    print(hasil)

printpenjumlahan(input("Masukkan NPM Anda: "))

#SOAL7
def printperkalian(npm):

    npm = list(map(int, npm))
    hasil = 0
    for n in npm:
        hasil *= n 
    print(hasil)

printperkalian(input("Masukkan NPM Anda: "))

#SOAL 8
#DigitGenap
def printNPMDigitGenap(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 ==0):
          if(n !=0):
              print(n, end = "")
printNPMDigitGenap(input("Masukan NPM anda :"))

#SOAL9
#DigitGanjil
def printNPMDigitGanjil(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 != 0):
              print(n, end = "")
printNPMDigitGanjil(input("Masukan NPM anda :"))

#SOAL10
def printNPMDigitPrima(npm):
    npm = list(map(int, npm))
    prima = []
    for n in npm:
        isPrime =  True
        if n == 0 or n == 1:
            isPrime = False
        for x in range(2, n):
            if n % x == 0:
                isPrime = False
        if isPrime:
            prima.append(n)
    
    for p in prima:
        print(p, end = "")
printNPMDigitPrima(input("Masukan NPM anda: "))
