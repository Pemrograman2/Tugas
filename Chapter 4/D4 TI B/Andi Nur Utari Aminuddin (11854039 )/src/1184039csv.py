# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 22:52:54 2019

@author: Lenovo
"""

import csv

#Jawaban No. 1
def bukaModeListCsv():
    with open('jwb1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[0], row[1], row[2]) 

#Jawaban No. 2            
def bukaModeDictCsv():
    with open('jwb1.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['npm'], row['nama'], row['kelas'])

def tulisCsv():
    with open('teori.csv', mode='w') as csv_file:
        fieldnames = ['npm', 'nama', 'kelas', 'tanggal lahir']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writeheader()
        writer.writerow({'npm': '1184039', 'nama': 'Andi', 'kelas': 'D4TI2A', 'tanggal lahir': '25/10/2000'})
        writer.writerow({'npm': '1184093', 'nama': 'Tari', 'kelas': 'D4TI2B', 'tanggal lahir': '25/01/2000'})
