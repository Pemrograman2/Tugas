def npm(npm):
    print (" +++++   +++++       +++++           +++++++        +++++       +++++++++++++      +++++       ")
    print (" +++++   +++++     +++++++++        ++++++++      +++++++++     +++++++++++++    +++++++++     ")
    print (" +++++   +++++    ++++   ++++      ++++ ++++     ++++   ++++    +++++++++++++   ++++   ++++    ")
    print (" +++++   +++++    ++++   ++++     ++++  ++++     ++++   ++++           ++++++   ++++   ++++    ")
    print (" +++++   +++++     +++++++++     ++++   ++++     ++++   ++++          ++++++          ++++     ")
    print (" +++++   +++++       +++++      ++++++++++++     ++++   ++++         ++++++          ++++      ")
    print (" +++++   +++++     +++++++++    ++++++++++++     ++++   ++++        ++++++          ++++       ")
    print (" +++++   +++++    ++++   ++++           ++++     ++++   ++++       ++++++          ++++        ")
    print (" +++++   +++++    ++++   ++++           ++++     ++++   ++++      ++++++          ++++         ")
    print (" +++++   +++++     +++++++++            ++++      +++++++++      ++++++          ++++++++++    ")
    print (" +++++   +++++       +++++              ++++        +++++       ++++++          +++++++++++    ")
    print (1184072%3)
    
def lur(npm) :
    npm = int(1184072)

    print ("input : ", npm)

    print ("output : ")

    for i in range (87) :
        print ("Hello, ", npm, "apa kabar ?")
        
def mulai(npm) :
    pms = "072"
    npm = 1184072
    jumlah = 0+7+2


    print ("0 + 7 + 2 = ", jumlah)

    print ("input : ", npm)
    
    print ("output : ")

    for i in range (jumlah) :
        print ("Hello, ",pms, "apa kabar ?")
        
def zero(npm) :
    npm = 1184072

    print ("input : ", npm)

    print ("output : ")

    for i in range (1) :
        print ("Hello, ",0, "apa kabar ?")
        
def abc(npm) :
    npm = "1184072"
    
    a=npm[0]
    b=npm[1]
    c=npm[2]
    d=npm[3]
    e=npm[4]
    f=npm[5]
    g=npm[6]

    for x in a,b,c,d,e,f,g, :
        print (x)
        
def jumlah(npm) :
    npm = "1184072"

    a=npm[0]
    b=npm[1]
    c=npm[2]
    d=npm[3]
    e=npm[4]
    f=npm[5]
    g=npm[6]
    y=1
    
    for x in a,b,c,d,e,f,g, :
        y+=int(x)
        print(y),
        
def perkalian(npm) :
    npm = "1184072"

    a=npm[0]
    b=npm[1]
    c=npm[2]
    d=npm[3]
    e=npm[4]
    f=npm[5]
    g=npm[6]
    y=1
    
    for x in a,b,c,d,e,f,g, :
        y*=int(x)
    print(y),
    
def genap(npm) :
    npm = "1184072"

    a=npm[0]
    b=npm[1]
    c=npm[2]
    d=npm[3]
    e=npm[4]
    f=npm[5]
    g=npm[6]

    for x in a,b,c,d,e,f,g, :
    
        if int(x)%2==0:
            if int(x)==0:
                x=""
            print(x,end ="")
            
def ganjil(npm) :
    npm = "1184072"

    a=npm[0]
    b=npm[1]
    c=npm[2]
    d=npm[3]
    e=npm[4]
    f=npm[5]
    g=npm[6]

    for x in a,b,c,d,e,f,g, :
        
        if int(x)%2==1:
            print(x,end ="")
            
def prima (npm):
    npm = "1184072"

    a=npm[0]
    b=npm[1]
    c=npm[2]
    d=npm[3]
    e=npm[4]
    f=npm[5]
    g=npm[6]

    for x in a,b,c,d,e,f,g, :
        if int(x)%2==1:
            for i in range(2,int(x)):
                if (int(x)%i) == 0:
                    break
            else :
                print(int(x),end =""),
            
try:
    prima(npm)
    ganjil(npm)
    genap(npm)
    perkalian(npm)
    jumlah(npm)
    abc(npm)
    zero(npm)
    mulai(npm)
    lur(npm)
    npm()

except ValueError:
    print("parameter tidak di isi")
