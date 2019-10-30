def bagi(a,b):
    c = a/b
    return c

satu = int(input("angka satu: "))
dua = int(input("angka dua: "))

try:
    print(pembagian(satu,dua))
except:
    print("Tidak bisa dibagi 0 (nol)")