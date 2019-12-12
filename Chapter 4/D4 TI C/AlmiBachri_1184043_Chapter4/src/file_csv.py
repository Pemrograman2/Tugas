# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 00:56:40 2019

@author: lovo
"""

import csv

def listCsv():
    with open('Almi.csv', 'r') as mahasiswa:
        python = csv.reader(mahasiswa)
        kobra_list = list(python)

    print(kobra_list)

def dictCsv():
    file_almi = csv.DictReader(open("Almi.csv"))

    for i in file_almi:
        print(i)

def writeCSV():
    with open('Almi.csv', 'w') as almi:
        tulis = csv.writer(almi)

        tulis.writerow(['Nama ', 'Jurusan', 'Tingkat'])
        tulis.writerow(['Almi', 'Mesin', 'Akhir'])

def openCSV():
    with open('viankereneuy.csv', 'r') as almimahasiswa:
        almi = csv.reader(almimahasiswa)

        for i in almi:
            print(i)