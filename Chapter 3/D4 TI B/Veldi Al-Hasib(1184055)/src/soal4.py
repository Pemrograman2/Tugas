def soal4(npm):
    key=npm%1000
    str_key=str(key)
    print("Halo, "+str_key[0]+" apa kabar ?")

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
soal4(npm)