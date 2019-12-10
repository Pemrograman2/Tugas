# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 12:12:40 2019

@author: USER
"""

import csv
#Soal1
def bukaModelistCsv():
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row['Npm'], row['Nama'], row['kelas'])
            
#soal2
def bukaModeDictCsv():
    with open('data.csv', mode='r') as csv_file:
         csv_reader = csv.DictReader(csv_file)        
         for row in csv_reader:
             print(row['Npm'], row['nama'], row['kelas'])
             
def tuisCsv():
    with open('data.csv', mode='w') as csv_file:
        fieldnames = ['Npm', 'nama', 'kelas', 'tanggal lahir']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerrow({'npm': '1184022', 'nama': 'echa', 'kelas': 'D4TI2B', 'tanggal lahir': '14/11/2001'})
        writer.writerrow({'npm': '1184086', 'nama': 'hanifah', 'kelas': 'D4TI2B', 'tanggal lahir': '25/03/2000'})
        
    