
#soal 1
def npm1():
    print("+++ +++  +++++  +++ +++ +++++++ +++++++ ++++++")
    print("+++ +++ +++ +++ +++ +++ +++ +++ +++        +++")
    print("+++ +++  +++++  +++++++ +++ +++ +++++++  +++++")
    print("+++ +++ +++ +++     +++ +++ +++ +++ +++    +++")
    print("+++ +++  +++++      +++ +++++++ +++++++ ++++++")
#soal 2
def npm2():
    npm=int(input("masukan NPM anda : "))
    TwoLastDigit=abs(npm)%100
    for i in range(TwoLastDigit):
       print("Halo, ", npm, " apa kabar ?")
#soal 3
def npm3():
    npm=int(input("Masukan NPM : "))
    key=str(npm%1000)
    print("Halo, "+str(npm)[4]+str(npm)[5]+str(npm)[6]+" apa kabar ?")

    for i in range(int(str(npm)[4])+int(str(npm)[5])+int(str(npm)[6])-1):
        print("Halo, "+str(npm)[4]+str(npm)[5]+str(npm)[6]+" apa kabar ?")
#soal 4
def npm4():
    npm=int(input("Masukan NPM : "))
    key=npm%1000
    str_key=str(key)
    print("Halo, "+str_key[0]+" apa kabar ?")
#soal 5
def npm5():
    i=0
    npm=input("Masukan NPM : ")
    while i<1:
        if len(npm) < 7:
            print("NPM Kurang dari 7 digit")
            npm=input("Masukan NPM : ")
        elif len(npm) > 7:
            print("NPM lebih dari 7 digit")
            npm=input("Masukan NPM : ")
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

#soal 6
def npm6():
    i=0
    npm=input("Masukan NPM : ")
    while i<1:
        if len(npm) < 7:
            print("NPM Kurang dari 7 digit")
            npm=input("Masukan NPM : ")
        elif len(npm) > 7:
            print("NPM lebih dari 7 digit")
            npm=input("Masukan NPM : ")
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
#soal 7
def npm7():
    i=0
    npm=input("Masukan NPM : ")
    while i<1:
        if len(npm) < 7:
            print("NPM Kurang dari 7 digit")
            npm=input("Masukan NPM : ")
        elif len(npm) > 7:
            print("NPM lebih dari 7 digit")
            npm=input("Masukan NPM : ")
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
#soal 8
def npm8():
    i=0
    npm=input("Masukan NPM : ")
    while i<1:
        if len(npm) < 7:
            print("NPM Kurang dari 7 digit")
            npm=input("Masukan NPM : ")
        elif len(npm) > 7:
            print("NPM lebih dari 7 digit")
            npm=input("Masukan NPM : ")
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
    
        if int(x)%2==0:
            if int(x)==0:
                x=""
            print(x,end ="")
#soal 9
def npm9():
    i=0
    npm=input("Masukan NPM : ")
    while i<1:
        if len(npm) < 7:
            print("NPM Kurang dari 7 digit")
            npm=input("Masukan NPM : ")
        elif len(npm) > 7:
            print("NPM lebih dari 7 digit")
            npm=input("Masukan NPM : ")
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
    
        if int(x)%2==1:
            print(x,end ="")
#soal 10
def npm10():
    i=0
    npm=input("Masukan NPM : ")
    while i<1:
        if len(npm) < 7:
            print("NPM Kurang dari 7 digit")
            npm=input("Masukan NPM : ")
        elif len(npm) > 7:
            print("NPM lebih dari 7 digit")
            npm=input("Masukan NPM : ")
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
        if int(x) > 1:
            for i in range(2,int(x)):
                if (int(x) % i) == 0:
                    break
            else:
                print(int(x),end =""),









