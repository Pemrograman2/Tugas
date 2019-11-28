def pembagian(a,b):
    c=a/b
    return c

d=int(input("pembilang : "))
e=int(input("penyebut : "))
try:
    print(pembagian(d,e))
except:
    print("jangan masukan angka 0")
