def Npm(npm):
    mod = int(npm) % 3 
    if mod == 0:
        print("*")
    elif mod == 1:
        print("#")
    elif mod == 2:
        print("+")


print("******   ******    *********   ***   ***  *********  ********* ********* ")
print("******   ******    ***   ***   ***   ***  ***   ***  ***       ***   *** ")
print("  ****     ****    *********   *********  ***   ***  ********* ********* ")
print("  ****     ****    *********   *********  ***   ***  ***   ***       *** ")
print("******** ********  ***   ***        ****  ***   ***  ***   ***       *** ")
print("******** ********  *********        ****  *********  ********* ********* ")

def ulang(npm):
    mod = int(npm) % 100
    for i in range(mod):
        print("hallo",npm,"apa kabar ?")

def ulangplus(npm):
    mod = int(npm)%1000
    string = str(mod)
    sub = npm[4] + npm[5] + npm[6]


    for i in range(int(npm[4])+int(npm[5])+int(npm[6])):
        print("hallo",npm[4] + npm[5] + npm[6],"apa kabar ?")

def ulangnol(npm):
    sub = npm[4]
        
    print("hallo",npm[4],"apa kabar")

def turun(npm):

    i = 0
    while i<1:
        if len(npm) < 7:
            print("npm kurang dari 7 digit, silahkan masukkan npm anda kembali")
        elif len(npm) > 7:
            print("npm yang diinputkan lebih dari 7, silahkan masukkan npm anda kembali")
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
        print(x,""),

def jumlah(npm):

    i = 0
    while i<1:
        if len(npm) < 7:
            print("npm kurang dari 7 digit, silahkan masukkan npm anda kembali")
        elif len(npm) > 7:
            print("npm yang diinputkan lebih dari 7, silahkan masukkan npm anda kembali")
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


def kali(npm):

    i = 0
    while i<1:
        if len(npm) < 7:
            print("npm kurang dari 7 digit, silahkan masukkan npm anda kembali")
        elif len(npm) > 7:
            print("npm yang diinputkan lebih dari 7, silahkan masukkan npm anda kembali")
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
        y*=int(x)
    print(y)

def genap(npm):

    i = 0
    while i<1:
        if len(npm) < 7:
            print("npm kurang dari 7 digit, silahkan masukkan npm anda kembali")
        elif len(npm) > 7:
            print("npm yang diinputkan lebih dari 7, silahkan masukkan npm anda kembali")
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

def ganjil(npm):

    i = 0
    while i<1:
        if len(npm) < 7:
            print("npm kurang dari 7 digit, silahkan masukkan npm anda kembali")
        elif len(npm) > 7:
            print("npm yang diinputkan lebih dari 7, silahkan masukkan npm anda kembali")
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

        if int(x)%3==0:
            if int(x)==0:
                x=""
            print(x,end ="")


    
    

        


    



