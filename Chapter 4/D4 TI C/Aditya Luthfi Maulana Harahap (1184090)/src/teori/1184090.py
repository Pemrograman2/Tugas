# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 18:24:33 2019

@author: Aditya Luthfi
"""

#Membaca File CSV dengan Fungsi reader dengan library CSV
import csv

with open('prak1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row[0], row[1], row[2])
        
#Membaca File CSV dengan Fungsi DictReader dengan library CSV
import csv

with open('prak1.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row['npm'], row['nama'], row['kelas'])
        
#Menulis File CSV dengan Fungsi writer dengan library CSV    
import csv

with open('prak2.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['npm', 'nama', 'kelas'])
    csv_writer.writerow(['1184090', 'Aditya Luthfi Maulana Harahap', 'D4TI2C'])
    csv_writer.writerow(['1184076', 'Ariq Rafi Kusumah', 'D4TI2C'])

#Menulis File CSV dengan Fungsi DictWriter dengan library CSV
import csv

with open('prak3.csv', mode='w') as csv_file:
    fieldnames = ['npm', 'nama', 'kelas']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'npm': '1184090', 'nama': 'Aditya Luthfi Maulana Harahap', 'kelas': 'D4TI2C'})
    writer.writerow({'npm': '1184076', 'nama': 'Ariq Rafi Kusumah', 'kelas': 'D4TI2A'})
    
#Membaca File CSV dengan Fungsi read_csv dengan Library Pandas
import pandas

df = pandas.read_csv('prak1.csv')
print(df)

#Menulis File CSV dengan Fungsi to_csv dengan Library Pandas
import pandas

df = pandas.read_csv('prak1.csv')
df.to_csv('prak4.csv')

#Membaca File CSV dengan Fungsi reader dengan library CSV
import csv

with open('prak1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row[0], row[1], row[2])
        
#Membaca File CSV dengan Fungsi DictReader dengan library CSV
import csv

with open('prak1.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row['npm'], row['nama'], row['kelas'])
        
#Menulis File CSV dengan Fungsi writer dengan library CSV    
import csv

with open('prak2.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['npm', 'nama', 'kelas'])
    csv_writer.writerow(['1184090', 'Aditya Luthfi Maulana Harahap', 'D4TI2C'])
    csv_writer.writerow(['1184076', 'Ariq Rafi Kusumah', 'D4TI2C'])

#Menulis File CSV dengan Fungsi DictWriter dengan library CSV
import csv

with open('prak3.csv', mode='w') as csv_file:
    fieldnames = ['npm', 'nama', 'kelas']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'npm': '1184090', 'nama': 'Aditya Luthfi Maulana Harahap', 'kelas': 'D4TI2C'})
    writer.writerow({'npm': '1184076', 'nama': 'Ariq Rafi Kusumah', 'kelas': 'D4TI2C'})
    
#Membaca File CSV dengan Fungsi read_csv dengan Library Pandas
import pandas

df = pandas.read_csv('prak1.csv')
print(df)

#Menulis File CSV dengan Fungsi to_csv dengan Library Pandas
import pandas

df = pandas.read_csv('prak1.csv')
df.to_csv('prak4.csv')#Membaca File CSV dengan Fungsi reader dengan library CSV
import csv

with open('prak1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row[0], row[1], row[2])
        
#Membaca File CSV dengan Fungsi DictReader dengan library CSV
import csv

with open('prak1.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row['npm'], row['nama'], row['kelas'])
        
#Menulis File CSV dengan Fungsi writer dengan library CSV    
import csv

with open('prak2.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['npm', 'nama', 'kelas'])
    csv_writer.writerow(['1184090', 'Aditya Luthfi Maulana Harahap', 'D4TI2C'])
    csv_writer.writerow(['1184076', 'Ariq Rafi Kusumah', 'D4TI2C'])

#Menulis File CSV dengan Fungsi DictWriter dengan library CSV
import csv

with open('prak3.csv', mode='w') as csv_file:
    fieldnames = ['npm', 'nama', 'kelas']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'npm': '1184090', 'nama': 'Aditya Luthfi Maulana Harahap', 'kelas': 'D4TI2C'})
    writer.writerow({'npm': '1184076', 'nama': 'Ariq Rafi Kusumah', 'kelas': 'D4TI2C'})
    
#Membaca File CSV dengan Fungsi read_csv dengan Library Pandas
import pandas

df = pandas.read_csv('prak1.csv')
print(df)

#Menulis File CSV dengan Fungsi to_csv dengan Library Pandas
import pandas

df = pandas.read_csv('prak1.csv')
df.to_csv('prak4.csv')