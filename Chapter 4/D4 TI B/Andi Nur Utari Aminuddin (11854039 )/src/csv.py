# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 23:13:03 2019

@author: Lenovo
"""
#Penggunaan Fungsi-Fungsi Format CSV

#Membaca file CSV dengan fungsi Reader dengan menggunaka library CSV
import csv 

with open('teori1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)

##Membaca File CSV dengan Fungsi DictReader dengan library CSV
import csv

with open('teori2.csv',mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row['npm'], row['nama'], row['kelas'])

        
#Menulis File CSV dengan Fungsi writer dengan library CSV    
import csv

with open('teori3.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['npm', 'nama', 'kelas'])
    csv_writer.writerow(['1184042', 'Andi Nur Annisa','2C'])
    csv_writer.writerow(['1234567','Andi Ahmad Zul Q','1A'])
    

#Menulis File CSV dengan Fungsi DictWriter dengan library CSV
import csv

with open('teori4.csv', mode='w') as csv_file:
    fieldnames = ['npm', 'nama', 'kelas']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'npm': '1184001', 'nama': 'Akil', 'kelas':'2B'})
    writer.writerow({'npm': '1184002', 'nama': 'Amin', 'kelas':'2A'})
    writer.writerow({'npm': '1184003', 'nama': 'Jeno', 'kelas':'2C'})
