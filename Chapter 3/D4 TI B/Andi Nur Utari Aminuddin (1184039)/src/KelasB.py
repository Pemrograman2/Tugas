class KelasB:
    jumlahMahasiswa = 0
    
    def __init__(self, npm, nama):
        self.npm = npm
        self.nama = nama
        KelasB.jumlahMahasiswa +=1
            
    def tampilkanProfil(self):
        print("Npm :", self.npm)
        print("Nama :", self.nama)
        print()