def NPM1():    
    print(" *** ***    ****     ***  ***   ******   ******    ********")
    print(" *** *** ***    ***  ***  ***  ***  *** ***  ***   *******")
    print(" *** ***    ****     ********  ***  *** ***  ***     ***")
    print(" *** *** ***    ***       ***  ***  *** ***  ***    ***")
    print(" *** ***    ****          ***   ******   ******    ***")
def NPM2(npm):
    NPM=int(npm)
    Tld=NPM%100 
    for i in range(Tld):  
        print("Halo ", NPM, " apa kabar ?")
def NPM3(npm):
    for i in range(int(str(npm)[4])+int(str(npm)[5])+int(str(npm)[6])):
        print("Halo, "+str(npm)[4]+str(npm)[5]+str(npm)[6]+" apa kabar ?")
    return None
def NPM4(npm):
    NPM = npm
    print("Halo, ",NPM[4]," Apa kabar?")
def NPM5(npm):
    i=0
    NPM = npm
    while i<1:
        if len(NPM)<7:
            print("Npm kurang dari 7!")
            NPM = input("Npm : ")
        elif len(NPM)>7:
            print("Npm lebih dari 7!")
            NPM = input("Npm : ")
        else:
            i=1
    A=NPM[0]
    B=NPM[1]
    C=NPM[2]
    D=NPM[3]
    E=NPM[4]
    F=NPM[5]
    G=NPM[6]
    for this in A,B,C,D,E,F,G:
        print(this)
def NPM6(npm):
    i=0
    NPM = npm
    while i<1:
        if len(NPM)<7:
            print("Npm kurang dari 7!")
            NPM = input("Npm : ")
        elif len(NPM)>7:
            print("Npm lebih dari 7!")
            NPM = input("Npm : ")
        else:
            i=1      
    A=NPM[0]
    B=NPM[1]
    C=NPM[2]
    D=NPM[3]
    E=NPM[4]
    F=NPM[5]
    G=NPM[6]
    X=0
    for this in A,B,C,D,E,F,G:
        X+=int(this)
    print(X)
def NPM7(npm):
    i=0
    NPM = npm
    while i<1:
        if len(NPM)<7:
            print("Npm kurang dari 7!")
            NPM = input("Npm : ")
        elif len(NPM)>7:
            print("Npm lebih dari 7!")
            NPM = input("Npm : ")
        else:
            i=1    
    A=NPM[0]
    B=NPM[1]
    C=NPM[2]
    D=NPM[3]
    E=NPM[4]
    F=NPM[5]
    G=NPM[6]
    X=1
    for this in A,B,C,D,E,F,G:
        X*=int(this)
    print(X)       
def NPM8(npm):
    i=0
    NPM = npm
    while i<1:
        if len(NPM)<7:
            print("Npm kurang dari 7!")
            NPM = input("Npm : ")
        elif len(NPM)>7:
            print("Npm lebih dari 7!")
            NPM = input("Npm : ")
        else:
            i=1
    A=NPM[0]
    B=NPM[1]
    C=NPM[2]
    D=NPM[3]
    E=NPM[4]
    F=NPM[5]    
    G=NPM[6]
    X=1
    for this in A,B,C,D,E,F,G:  
        if int(this)%2==0:
            if int(this)==0:
                this=""
            print(this,end =" ")
def NPM9(npm):
    i=0
    NPM = npm
    while i<1:
        if len(NPM)<7:
            print("Npm kurang dari 7!")
            NPM = input("Npm : ")
        elif len(NPM)>7:
            print("Npm lebih dari 7!")
            NPM = input("Npm : ")
        else:
            i=1
    A=NPM[0]
    B=NPM[1]
    C=NPM[2]
    D=NPM[3]
    E=NPM[4]
    F=NPM[5]
    G=NPM[6]
    X=1
    for this in A,B,C,D,E,F,G:    
        if int(this)%2==1:
            print(this,end=" ")
def NPM10(npm):
    i=0
    NPM = npm
    while i<1:
        if len(NPM)<7:
            print("Npm kurang dari 7!")
            NPM = input("Npm : ")
        elif len(NPM)>7:
            print("Npm lebih dari 7!")
            NPM = input("Npm : ")
        else:
            i=1
    A=NPM[0]
    B=NPM[1]
    C=NPM[2]
    D=NPM[3]
    E=NPM[4]
    F=NPM[5]
    G=NPM[6]
    X=1
    for x in A,B,C,D,E,F,G:    
        if int(X) > 1:
            for i in range(2,int(X)):
                if (int(X) % i) == 0:
                    break
            else:
                print(int(X),end =""),    