# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 20:30:49 2019

@author: Putri Nella
"""

import csv
#No.1
def MembukaModeListCsv():
    with open('Teori1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[0], row[1], row[2], row[3])

#\No.2
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
        writer.writerow({'npm': '1184022', 'nama': 'pp', 'kelas': 'D4TI2E', 'tanggal lahir': '23/07/2000'})
        writer.writerow({'npm': '1184003', 'nama': 'aa', 'kelas': 'D4TI2E', 'tanggal lahir': '27/08/2000'})
    