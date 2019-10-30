def pembagian(a,b):
    c=a/b
    return c

d=int(input("angka pertama : "))
e=int(input("angka kedua : "))
try:
    print(pembagian(d,e))
except:
    print("jangan masukan angka 0")
