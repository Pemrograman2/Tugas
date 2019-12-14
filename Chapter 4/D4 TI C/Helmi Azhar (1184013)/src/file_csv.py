# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 23:14:50 2019

@author: Asus
"""

import csv

def listCsv():
    with open('Helmi.csv', 'r') as mahasiswa:
        python = csv.reader(mahasiswa)
        kobra_list = list(python)

    print(kobra_list)

def dictCsv():
    file_Helmi = csv.DictReader(open("Helmi.csv"))

    for i in file_Helmi:
        print(i)

def writeCSV():
    with open('Helmi.csv', 'w') as Helmi:
        tulis = csv.writer(Helmi)

        tulis.writerow(['Nama ', 'Jurusan', 'Semester'])
        tulis.writerow(['Helmi', 'Musik', 'Awal'])

def openCSV():
    with open('Helmi.csv', 'r') as mhs:
        Helmi = csv.reader(mhs)

        for i in Helmi:
            print(i)