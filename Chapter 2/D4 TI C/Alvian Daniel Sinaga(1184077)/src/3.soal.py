npm=int(input("Masukan NPM : "))
key=str(npm%1000)
print("Halo, "+str(npm)[4]+str(npm)[5]+str(npm)[6]+" apa kabar ?")

for i in range(int(str(npm)[4])+int(str(npm)[5])+int(str(npm)[6])-1):
    print("Halo, "+str(npm)[4]+str(npm)[5]+str(npm)[6]+" apa kabar ?")