def pembagian(p,q):
    z=p/q
    return z

a=int(input("angka pertama : "))
b=int(input("angka kedua : "))
try:
    print(pembagian(a,b))
except:
    print("jangan masukan angka 0")
