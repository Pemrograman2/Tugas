#soal 1
def npm1(npm):
    
    print("###  ###  #########  ###   ###  #########  #########    #########")
    print("###  ###  #########  ###   ###  #########  #########    #########")
    print("###  ###  ###   ###  ###   ###  ###   ###        ###    ###")
    print("###  ###  ###   ###  ###   ###  ###   ###        ###    ###")
    print("###  ###  #########  #########  ###   ###  #########    #########")
    print("###  ###  ###   ###        ###  ###   ###  ###          ###   ###")
    print("###  ###  ###   ###        ###  ###   ###  ###          ###   ###")
    print("###  ###  #########        ###  #########  #########    #########")
    print("###  ###  #########        ###  #########  #########    #########")

#soal 2
def npm2(npm):
    npm = input ("Masukan NPM Anda: ")
    
    nPm = int(npm[-2:])
    
    for a in range(nPm):
        print("Halo, " + npm + " apa kabar?")

#soal 3
def npm3(npm):
    npm = input ("Masukan NPM Anda: ")
    
    nPm = npm[-3:]
    
    b = 0
    
    for i in nPm:
        c = int(i) + b
        b = c
        
    for i in range(b):
        print ("Hallo, "+ nPm + "Apa Kabar?")
     
#soal 4    
def npm4(npm):
    npm = input ("Masukan NPM Anda: ")
    
    
    nPm = npm[-3]
    
    for i in nPm:
        print("Halo, " + nPm + " apa kabar?")

#soal 5    
def npm5(npm):
    npm = input ("Masukan NPM Anda: ")
    
    for i in npm:
        print(i)    

#soal 6
def npm6(npm):
    npm = input ("Masukan NPM Anda: ")
    
    a = 0
    b = 0
    for i in npm:
        c = int(i) + b
        b = c
        a += 1
    
    print(b)

#soal 7
def npm7(npm):
    npm = input ("Masukan NPM Anda: ")
    
    a = 0
    b = 0
    for i in npm:
        c = int(i) * b
        b = c
        a += 1

    print(b)

#soal 8
def npm8(npm):
    npm = input("Masukan NPM Anda: ")
    
    for i in npm:
        a = int(i)
    
        if a != 0:
            if a % 2 == 0:
                print(i, end="")

#soal 9            
def npm9(npm):
    npm = input("Masukan NPM anda: ")
    
    for i in npm:
        a = int(i)
    
        if a != 0:
            if a % 2 == 1:
                print(i, end="")

#soal10
def npm10(npm):
    npm = input("Masukan NPM Anda: ")
    
    for i in npm:
    
        number = int(i)
    
        if number > 1:
    
            for i in range(2, number):
                if (number % i) == 0:
                    break
            else:
                print(number)