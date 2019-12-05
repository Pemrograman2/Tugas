npm=int(input("masukkan NPM anda :"))
TwoLastDigit=abs(npm)%100
for i in range(TwoLastDigit):
    print("Halo, ", npm, "Apa kabar?")