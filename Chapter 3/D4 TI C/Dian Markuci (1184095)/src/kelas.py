# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 22:04:56 2019

@author: ASUS
"""

 class Mahasiswa:
    totalMahasiswa = 0
    
    def __init__(self, npm, nama):
        self.npm = npm
        self.nama = nama
        Mahasiswa.totalMahasiswa +=1
        
    def tampilkanProfil(self):
        print("NPM :", self.npm)
        print("Nama :", self.nama)
        print() 
        
    mahasiswa1 = totalMahasiswa("1184065", "Etika Khusnul Laeli")
    mahasiswa2 = totalMahasiswa("1184030", "Dyning Aida Batrishya")
    
    mahasiswa1.tampilkanProfil()
    mahasiswa2.tampilkanProfil()
    
print("Jumlah mahasiswa adalah ", Mahasiswa.totalMahasiswa)
