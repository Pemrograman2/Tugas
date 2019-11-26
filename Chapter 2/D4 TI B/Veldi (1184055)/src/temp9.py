
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
        
Q=NPM[0]
W=NPM[1]
E=NPM[2]
R=NPM[3]
T=NPM[4]
I=NPM[5]
O=NPM[6]

X=1

for this in Q,W,E,R,T,I,O:
   
    if int(this)%2==0:
        if int(this)==0:
            this=""
        print(this,end =" ")    
        