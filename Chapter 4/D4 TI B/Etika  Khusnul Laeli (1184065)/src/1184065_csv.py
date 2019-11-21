# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 00:19:25 2019

@author: ANIF
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
        writer.writerow({'npm': '1184002', 'nama': 'Nathan', 'kelas': 'D4TI2C', 'tanggal lahir': '12/12/2000'})
        writer.writerow({'npm': '1184003', 'nama': 'Januar', 'kelas': 'D4TI2B', 'tanggal lahir': '6/6/2000'})
    