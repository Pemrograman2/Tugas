# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 01:56:16 2019

@author: ANIF
"""
from folder.Mahasiswa import Mahasiswa

mhs = Mahasiswa("1184065", "Etika Khusnul Laeli")

mhs.tampilkanProfil()

print("Jumlah mahasiswa adalah ", Mahasiswa.totalMahasiswa)