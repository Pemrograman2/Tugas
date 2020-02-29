# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 18:04:11 2020

@author: Asus
"""

import csv

def listCsv():
    with open('ariqkereneuy.csv', 'r') as mahasiswa:
        batu = csv.reader(mahasiswa)
        pasir_list = list(batu)

    print(pasir_list)

def dictCsv():
    file_ariq = csv.DictReader(open("ariqkereneuy.csv"))

    for i in file_ariq:
        print(i)

def writeCSV():
    with open('ariqkereneuy.csv', 'w') as ariqmahbebas:
        tulis = csv.writer(ariqmahbebas)

        tulis.writerow(['Nama Mahasiswa', 'pendidikan', 'berat'])
        tulis.writerow(['ariq', 'D4', '50'])

def openCSV():
    with open('ariqkereneuy.csv', 'r') as ariqmahasiswa:
        ariqkeren = csv.reader(ariqmahasiswa)

        for i in ariqkeren:
            print(i)