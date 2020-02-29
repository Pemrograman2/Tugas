# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 18:00:54 2020

@author: Asus
"""

import csv

def listCsv():
    with open('ariqmahasiswa.csv', 'R') as mahasiswa:
        batu = csv.reader(mahasiswa)
        pasir_list = list(maca)

    print(pasir_list)

def dictCsv():
    file_ariq = csv.DictReader(open("ariqmahasiswa.csv"))

    for i in file_ariq:
        print(i)

def writeCSV():
    with open('ariqmahasiswa.csv', 'W') as ariqmahbebas:
        tulis = csv.writer(ariqmahbebas)

        tulis.writerow(['NamaMahasiswa', 'jenis', 'tinggi','berat'])
        tulis.writerow(['ariq', 'laki', '167','50'])

def openCSV():
    with open('ariqmahasiswa.csv', 'R') as ariqnmahasiswa:
        ariqkeren = csv.reader(ariqmahasiswa)

        for i in ariqkeren:
            print(i)