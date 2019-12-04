# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 17:56:17 2019

@author: Aditya Luthfi
"""

#Membaca File CSV dengan Fungsi reader dengan library CSV
import csv

with open('praktikum1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row[0], row[1], row[2])
        
#Membaca File CSV dengan Fungsi DictReader dengan library CSV
import csv

with open('praktikum1.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row['npm'], row['nama'], row['kelas'])
        
#Menulis File CSV dengan Fungsi writer dengan library CSV    
import csv

with open('praktikum2.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['npm', 'nama', 'kelas'])
    csv_writer.writerow(['1184001', 'Messi', 'D4TI2C'])
    csv_writer.writerow(['1184002', 'Dembele', 'D4TI2C'])

#Menulis File CSV dengan Fungsi DictWriter dengan library CSV
import csv

with open('praktikum3.csv', mode='w') as csv_file:
    fieldnames = ['npm', 'nama', 'kelas']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'npm': '1184091', 'nama': 'Suarez', 'kelas': 'D4TI2C'})
    writer.writerow({'npm': '1184092', 'nama': 'Gerizmen', 'kelas': 'D4TI2C'})
    
#Membaca File CSV dengan Fungsi read_csv dengan Library Pandas
import pandas

df = pandas.read_csv('praktikum1.csv')
print(df)

#Menulis File CSV dengan Fungsi to_csv dengan Library Pandas
import pandas

df = pandas.read_csv('praktikum1.csv')
df.to_csv('praktikum4.csv')
    
#Fungsi Try Except 
def bacaCsvPandas():
    try:
        df = pandas.read_csv('praktikum1.csv')
        print(dt)
    except SyntaxError:
        print("Kesalahan penulisan (syntax)")
    except NameError:
        print("Variable tidak ada")
    except TypeError:
        print("Tipe data salah")
    except:
        print("Terjadi sebuah kesalahan")

bacaCsvPandas()