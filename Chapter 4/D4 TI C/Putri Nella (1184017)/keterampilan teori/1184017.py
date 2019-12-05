# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 20:29:58 2019

@author: Putri Nella
"""

#Membaca File Csv dengan fungsi reader library csv
import csv

with open('Teori1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row[0], row[1], row[2])

#Membaca File Csv dengan fungsi Dict Reader dengan library CSV
import csv

with open('Teori1.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row['npm'], row['nama'], row['kelas'])

#Menullis File CSV dengan Fungsi Writer dengan library CSV
import csv

with open('Teori2.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['npm', 'nama', 'kelas'])
    csv_writer.writerow(['11840165', 'Rasya Athaya', 'D4TI2C'])
    csv_writer.writerow(['11840130', 'Khusnul Laeli', 'D4TI2B'])

#Menulis File CSV dengan Fungsi DictWriter dengan library csv
import csv

with open('Teori3.csv', mode='w') as csv_file:
    fieldnames = ['npm', 'nama', 'kelas']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({'npm': '1184038','nama':'Nurul Kamila', 'kelas':'D4TI2C'})
    writer.writerow({'npm': '1184017', 'nama':'Putri Nella', 'kelas':'D4TI2C'})

#Membaca File CSV dengan fungsi read_csv dengan library pandas
import pandas

df = pandas.read_csv('Teori1.csv')
print(df)

#Menulis File CSV dengan fungsi to_csv dengan library pandas
import pandas

df = pandas.read_csv('Teori1.csv')
df.to_csv('Teori4.csv')

#Fungsi Try Except
def bacaCsvPandas():
    try:
        dt = pandas.read_csv('teori.csv')
        print(dt)
    except SyntaxError:
        print("Kesalahan penulisan syntax")
    except NameError:
        print("Variabel tersebut tidak ada")
    except TypeError:
        print("Tipe Data Salah")
    except:
        print("Terjado sebuah kesalahan")

bacaCsvPandas()