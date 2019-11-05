# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 01:41:54 2019

@author: ANIF
"""
class Mahasiswa:
    totalMahasiswa = 0
    
    def __init__(self, npm, nama):
        self.npm = npm
        self.nama = nama
        Mahasiswa.totalMahasiswa +=1
        
    def tampilkanProfil(self):
        print("NPM :",self.npm)
        print("NPM :",self.nama)
        print()
        
    mahasiswa = Mahasiswa("1184065", "Etika Khusnul Laeli")
    
    mahasiswa.tampilkanProfil()
    
    print("Jumlah mahasiswa adalah ", Mahasiswa.totalMahasiswa)
