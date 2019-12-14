# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 23:01:01 2019

@author: Asus
"""

import csv

def listCsv():
    with open('mhs.csv', 'R') as mahasiswa:
        python= csv.reader(mahasiswa)
        kobra_list = list(baca)

    print(kobra_list)

def dictCsv():
    file_Helmi = csv.DictReader(open("mhs.csv"))

    for i in file_Helmi:
        print(i)

def writeCSV():
    with open('mhs.csv', 'W') as Helmi:
        tulis = csv.writer(Helmi)

        tulis.writerow(['Npm', 'Nama', 'Jurusan',])
        tulis.writerow(['14', 'Mariong', 'Tari'])

def openCSV():
    with open('mhs.csv', 'R') as mhs:
        Helmi = csv.reader(mhs)

        for i in Helmi:
            print(i)