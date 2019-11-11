# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 22:22:11 2019

@author: Ahmad Agung Tawakkal
"""

import csv

#Jawaban No. 1
def bukaModeListCsv():
    with open('praktikum.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[0], row[1], row[2])

#Jawaban No. 2            
def bukaModeDictCsv():
    with open('praktikum.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['npm'], row['nama'], row['kelas'])

def tulisCsv():
    with open('praktikum5.csv', mode='w') as csv_file:
        fieldnames = ['npm', 'nama', 'kelas', 'tanggal lahir']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writeheader()
        writer.writerow({'npm': '1184005', 'nama': 'Ter Stegen', 'kelas': 'D4TI2B', 'tanggal lahir': '30/03/2000'})
        writer.writerow({'npm': '1184006', 'nama': 'Coutinho', 'kelas': 'D4TI2B', 'tanggal lahir': '30/04/2000'})
