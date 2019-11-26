# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 21:19:57 2019

@author: NISA
"""

import csv
#Jawaban No.1
def MembukaModeListCsv():
    with open('Teori1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[0], row[1], row[2], row[3])

#Jawaban No.2
def MembukaModeDictCsv():
    with open('Teori1.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['npm'],row['nama'],row['kelas'], row['tanggal lahir'])

def tulisCsv():
    with open('Teori6.csv', mode='w') as csv_file:
        fieldnames = ['npm', 'nama', 'kelas', 'tanggal lahir']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
       
        writer.writeheader()
        writer.writerow({'npm': '1184022', 'nama': 'Tantri Pratami', 'kelas': 'D4TI2D', 'tanggal lahir': '08/01/2001'})
        writer.writerow({'npm': '1184003', 'nama': 'Nafila Awlya', 'kelas': 'D4TI2D', 'tanggal lahir': '22/01/2000'})
    