#No.1
def namafungsi1(inputanFungsi):
    return inputanFungsi
output = namafungsi1("kembalian dari fungsi")
print(output)

#No.2
#moduldaripythonOS
import os
print("Nama os adalah: ", os.name)


#No.3
#class 
class B:
#attribute
    mahasiswa = 'Teknik Informatika'
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm
Tari = B("Tari", 1184039)
Akil = B("Akil", 1184041)
print("{} npm : {} dan {} npm : {}.".format(
    Tari.nama, Tari.npm, Akil.nama, Akil.npm))
if Tari.mahasiswa == "Teknik Informatika":
    print("{0} adalah mahasiswa prodi {1}!".format(Tari.nama, Tari.mahasiswa))

#No.4
from KelasB import KelasB
mahasiswa = KelasB("1184039", "Andi Nur Utari")
mahasiswa = KelasB("1184041", "Akil Munawwar")

mahasiswa.tampilkanProfil()
mahasiswa.tampilkanProfil()
print("Total mahasiswa : ", KelasB.jumlahMahasiswa)

#No.5
from kalkulator import Perkalian
hasil = Perkalian(25, 10)
print(hasil)

#No.6 
import kalkulator
a=25
b=10

hasil1=kalkulator.Penambahan(a,b)
hasil2=kalkulator.Pengurangan(a,b)
hasil3=kalkulator.Perkalian(a,b)
hasil4=kalkulator.Pembagian(a,b)

print(hasil1)
print(hasil2)
print(hasil3)
print(hasil4)

#No.7
from Folder.KelasB import KelasB
mahasiswa = KelasB("1184039", "Andi Nur Utari")
mahasiswa = KelasB("1184041", "Akil Munawwar")

mahasiswa.tampilkanProfil()
mahasiswa.tampilkanProfil()
print("Total mahasiswa : ", KelasB.jumlahMahasiswa)


