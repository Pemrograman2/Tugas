# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 20:38:00 2019

@author: Putri Nella
"""
#Membaca File CSV dengan Fungsi DictReader dengan library CSV
import csv

with open('Teori1.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row['npm'], row['nama'], row['kelas'])
