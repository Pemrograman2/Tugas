# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 01:06:18 2019

@author: ANIF
"""

class Mahasiswa:
    totalMahasiswa = 0
    
    def __init__(self, npm, nama):
        self.npm = npm
        self.nama = npm
        Mahasiswa.totalMahasiswa +=1
        
    def tampilkanProfil(self):
        print("NPM :", self.npm)
        print("NPM :", self.nama)
        print()