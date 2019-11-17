import kls3lib
import lib3


npm=input("Input NPM : ")
i=0
while i<1:
    if len(npm) < 7:
        print("NPM Kurang dari 7 digit")
        npm=input("Input NPM : ")
    elif len(npm) > 7:
        print("NPM lebih dari 7 digit")
        npm=input("Input NPM : ")
    else:
        i=1

#Contoh pemanggilan fungsi pada class
cobakelas=kls3lib.Kelas3lib(npm) 
hasilkelas=cobakelas.npm1()

print("")

#Contoh pemanggilan fungsi pada library
lib3.kali(npm)
lib3.turun(npm)
