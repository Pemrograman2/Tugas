# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 11:41:08 2019

@author: Ahmad Agung Tawakkal
"""

#Membaca File CSV dengan Fungsi reader dengan library CSV
import csv

with open('praktikum.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row[0], row[1], row[2])
        
#Membaca File CSV dengan Fungsi DictReader dengan library CSV
import csv

with open('praktikum.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row['npm'], row['nama'], row['kelas'])
        
#Menulis File CSV dengan Fungsi writer dengan library CSV    
import csv

with open('praktikum2.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['npm', 'nama', 'kelas'])
    csv_writer.writerow(['1184015', 'Ahmad Agung Tawakkal', 'D4TI2B'])
    csv_writer.writerow(['1184041', 'Akil Munawwar'       , 'D4TI2B'])

#Menulis File CSV dengan Fungsi DictWriter dengan library CSV
import csv

with open('praktikum3.csv', mode='w') as csv_file:
    fieldnames = ['npm', 'nama', 'kelas']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'npm': '1184015', 'nama': 'Ahmad Agung Tawakkal', 'kelas': 'D4TI2A'})
    writer.writerow({'npm': '1184041', 'nama': 'Akil Munawwar'       , 'kelas': 'D4TI2A'})
    
#Membaca File CSV dengan Fungsi read_csv dengan Library Pandas
import pandas

df = pandas.read_csv('praktikum.csv')
print(df)

#Menulis File CSV dengan Fungsi to_csv dengan Library Pandas
import pandas

df = pandas.read_csv('praktikum.csv')
df.to_csv('praktikum4.csv')

#Membaca File CSV dengan Fungsi reader dengan library CSV
import csv

with open('praktikum.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row[0], row[1], row[2])
        
#Membaca File CSV dengan Fungsi DictReader dengan library CSV
import csv

with open('praktikum.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row['npm'], row['nama'], row['kelas'])
        
#Menulis File CSV dengan Fungsi writer dengan library CSV    
import csv

with open('praktikum2.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['npm', 'nama', 'kelas'])
    csv_writer.writerow(['1184015', 'Ahmad Agung Tawakkal', 'D4TI2B'])
    csv_writer.writerow(['1184041', 'Akil Munawwar'       , 'D4TI2B'])

#Menulis File CSV dengan Fungsi DictWriter dengan library CSV
import csv

with open('praktikum3.csv', mode='w') as csv_file:
    fieldnames = ['npm', 'nama', 'kelas']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'npm': '1184015', 'nama': 'Ahmad Agung Tawakkal', 'kelas': 'D4TI2A'})
    writer.writerow({'npm': '1184041', 'nama': 'Akil Munawwar'       , 'kelas': 'D4TI2A'})
    
#Membaca File CSV dengan Fungsi read_csv dengan Library Pandas
import pandas

df = pandas.read_csv('praktikum.csv')
print(df)

#Menulis File CSV dengan Fungsi to_csv dengan Library Pandas
import pandas

df = pandas.read_csv('praktikum.csv')
df.to_csv('praktikum4.csv')#Membaca File CSV dengan Fungsi reader dengan library CSV
import csv

with open('praktikum.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row[0], row[1], row[2])
        
#Membaca File CSV dengan Fungsi DictReader dengan library CSV
import csv

with open('praktikum.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row['npm'], row['nama'], row['kelas'])
        
#Menulis File CSV dengan Fungsi writer dengan library CSV    
import csv

with open('praktikum2.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['npm', 'nama', 'kelas'])
    csv_writer.writerow(['1184015', 'Ahmad Agung Tawakkal', 'D4TI2B'])
    csv_writer.writerow(['1184041', 'Akil Munawwar'       , 'D4TI2B'])

#Menulis File CSV dengan Fungsi DictWriter dengan library CSV
import csv

with open('praktikum3.csv', mode='w') as csv_file:
    fieldnames = ['npm', 'nama', 'kelas']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'npm': '1184015', 'nama': 'Ahmad Agung Tawakkal', 'kelas': 'D4TI2A'})
    writer.writerow({'npm': '1184041', 'nama': 'Akil Munawwar'       , 'kelas': 'D4TI2A'})
    
#Membaca File CSV dengan Fungsi read_csv dengan Library Pandas
import pandas

df = pandas.read_csv('praktikum.csv')
print(df)

#Menulis File CSV dengan Fungsi to_csv dengan Library Pandas
import pandas

df = pandas.read_csv('praktikum.csv')
df.to_csv('praktikum4.csv')

