def NPM10():
    i=0
    NPM = input("Npm : ")
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

