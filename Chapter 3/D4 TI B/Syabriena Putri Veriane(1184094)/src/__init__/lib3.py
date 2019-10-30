#soal1
def NPM1():
    npm = input("NPM: ")
    val = int(npm)
    
    modulus = val % 3
    print("Modulus Npm anda: ")
    print(modulus)
    
    if (modulus == 0):
        print("*** *** ******** ***  *** ********* ******** ***  ***")
        print("*** *** **    ** ***  *** ***   *** ***  *** ***  ***")
        print("*** *** ******** ******** ***   *** ******** ********")
        print("*** *** **    **      *** ***   ***      ***      ***")
        print("*** *** ********      *** ********* ********      ***")
        
#soal2
def NPM2():
    npm = input("NPM: ")
    val = int(npm[5:7])
    
    print("Input: "+npm)
    print("Output: ")
    
    while val > 0:
        print("Hallo, "+npm+" Apa Kabar?")
        val = val - 1
        
#soal3
def NPM3():    
    npm = input("NPM: ")
    
    val = int(npm[4])
    val2 = int(npm[5])
    val3 = int(npm[6])
    
    subs = val + val2 + val3
    
    print("Input: "+npm)
    print("Output: ")
    
    while subs > 0:
        print("Hallo, "+npm[4:7]+" Apa Kabar?")
        subs = subs - 1

#soal4
def NPM4():
    npm = input("NPM: ")
    
    print("Input: "+npm)
    print("Output: ")
    print("Hallo, "+npm[4]+" Apa Kabar?")

#soal5
def NPM5():
    i=0
    npm = input("NPM: ")
    while i<1:
        if len(npm)<7:
            print("npm kurang dari 7")
            npm = input("NPM: ")
        elif len(npm)>7:
            print("npm lebih dari 7")
            npm = input("NPM: ")
        else:
            i=1
            
    a=npm[0]
    b=npm[1]
    c=npm[2]
    d=npm[3]
    e=npm[4]
    f=npm[5]
    g=npm[6]
    
    for x in a,b,c,d,e,f,g:
        print(x, end = ""),

#soal6
def NPM6():
    i=0
    npm = input("NPM: ")
    while i<1:
        if len(npm)<7:
            print("npm kurang dari 7")
            npm = input("NPM: ")
        elif len(npm)>7:
            print("npm lebih dari 7")
            npm = input("NPM: ")
        else:
            i=1
            
    a=npm[0]
    b=npm[1]
    c=npm[2]
    d=npm[3]
    e=npm[4]
    f=npm[5]
    g=npm[6]
    
    y=0
    
    
    for x in a,b,c,d,e,f,g:
        y+=int(x)
    print(y)
    
#soal7
def NPM7():
    i=0
    npm = input("NPM: ")
    while i<1:
        if len(npm)<7:
            print("npm kurang dari 7")
            npm = input("NPM: ")
        elif len(npm)>7:
            print("npm lebih dari 7")
            npm = input("NPM: ")
        else:
            i=1
            
    a=npm[0]
    b=npm[1]
    c=npm[2]
    d=npm[3]
    e=npm[4]
    f=npm[5]
    g=npm[6]
    
    conv=1
    
    for x in a,b,c,d,e,f,g:
        conv*=int(x)
    print(conv)

#soal8
def NPM8():
    i=0
    npm = input("NPM: ")
    while i<1:
        if len(npm)<7:
            print("npm kurang dari 7")
            npm = input("NPM: ")
        elif len(npm)>7:
            print("npm lebih dari 7")
            npm = input("NPM: ")
        else:
            i=1
            
    a=npm[0]
    b=npm[1]
    c=npm[2]
    d=npm[3]
    e=npm[4]
    f=npm[5]
    g=npm[6]
    
    for x in a,b,c,d,e,f,g:
        print(x)
    
#soal9
def NPM9():
    i=0
    npm = input("NPM: ")
    while i<1:
        if len(npm)<7:
            print("npm kurang dari 7")
            npm = input("NPM: ")
        elif len(npm)>7:
            print("npm lebih dari 7")
            npm = input("NPM: ")
        else:
            i=1
            
    a=npm[0]
    b=npm[1]
    c=npm[2]
    d=npm[3]
    e=npm[4]
    f=npm[5]
    g=npm[6]
    
    
    for x in a,b,c,d,e,f,g:
        
        if int(x)%2==0:
            if int(x)==0:
                x=""
            print(x,end ="")

#soal10
def NPM10():
    i=0
    npm = input("NPM: ")
    while i<1:
        if len(npm)<7:
            print("npm kurang dari 7")
            npm = input("NPM: ")
        elif len(npm)>7:
            print("npm lebih dari 7")
            npm = input("NPM: ")
        else:
            i=1
            
    a=npm[0]
    b=npm[1]
    c=npm[2]
    d=npm[3]
    e=npm[4]
    f=npm[5]
    g=npm[6]
    
    
    
    for x in a,b,c,d,e,f,g:
        
        if int(x)%2==1:
            print(x,end="")

#soal11
def NPM11():
    i=0
    npm = input("NPM: ")
    while i<1:
        if len(npm)<7:
            print("npm kurang dari 7")
            npm = input("NPM: ")
        elif len(npm)>7:
            print("npm lebih dari 7")
            npm = input("NPM: ")
        else:
            i=1
            
    a=npm[0]
    b=npm[1]
    c=npm[2]
    d=npm[3]
    e=npm[4]
    f=npm[5]
    g=npm[6]
    
    for x in a,b,c,d,e,f,g:
        if int(x) > 1:
            for i in range(2,int(x)):
                if (int(x) % i) == 0:
                    break
            else:
                print(int(x),end ="")