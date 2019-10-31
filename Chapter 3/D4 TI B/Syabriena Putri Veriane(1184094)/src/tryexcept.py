def bagi(a.t):
    b = a/t
    return b

siji = int(input("angka 1: "))
loro = int(input("angka 2: "))

try:
    print(pembagi(siji,loro))
except:
    print("tidak bisa dibagi 0")