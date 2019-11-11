def Pembagian(a,b):
    r = a / b
    return r

try:
    Pembagian(17,0)
except Exception as e:
    pass
print("angka yang anda masukkan tidak tepat")