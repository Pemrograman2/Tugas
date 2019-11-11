def npm4(npm):
    isinya=int(npm%1000)
    str_key=str(isinya)
    print("Halo, "+str_key[0]+" apa kabar ?")

b=0
npm=input("Masukkan NPM kamu : ")
while b<1:
    if len(npm) < 7:
        print("NPM kamu kurang dari 7 digit")
        npm=input("Masukan NPM kamu : ")
    elif len(npm) > 7:
        print("NPM kamu lebih dari 7 digit")
        npm=input("Masukan NPM kamu : ")
    else:
        b=1
npm4(npm)