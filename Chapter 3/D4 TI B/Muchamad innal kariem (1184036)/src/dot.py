def pembagian(a,b):
    c=a/b
    return c

f=int(input("angka pertama : "))
g=int(input("angka kedua : "))
try:
    print(pembagian(f,g))
except:
    print("jangan masukan angka 0")
