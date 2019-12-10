# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 00:24:52 2019

@author: lovo
"""

import csv

def listCsv():
    with open('mhs.csv', 'R') as mahasiswa:
        python= csv.reader(mahasiswa)
        kobra_list = list(baca)

    print(kobra_list)

def dictCsv():
    file_almi = csv.DictReader(open("mhs.csv"))

    for i in file_almi:
        print(i)

def writeCSV():
    with open('mhs.csv', 'W') as almi:
        tulis = csv.writer(almi)

        tulis.writerow(['Npm', 'Nama', 'Jurusan',])
        tulis.writerow(['118666', 'DadangKonelo', 'TataBoga'])

def openCSV():
    with open('mhs.csv', 'R') as mhs:
        almi = csv.reader(mhs)

        for i in almi:
            print(i)