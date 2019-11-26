# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 22:04:52 2019

@author: NISA
"""

#Membaca File CSV dengan Fungsi DictReader dengan library CSV
import csv

with open('Teori1.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row['npm'], row['nama'], row['kelas'])