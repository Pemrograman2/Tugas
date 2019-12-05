# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 20:27:16 2019

@author: Putri Nella
"""
import csv
#No.1
def MembukaModeListCsv():
    with open('Teori1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[0], row[1], row[2])

#No.2
def MembukaModeDictListCsv():
    with open('Teori1.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['npm'], row['nama'], row['kelas'])

#Fungsi Try Except
def buatBacaCsvPandas():
    try:
        dt = pandas.read_csv('teori1.csv')
        print(dt)
    except SyntaxError:
        print("Kesalahan penulisan syntax")
    except NameError:
        print("Variable tersebut tidak ada")
    except TypeError:
        print("Tipe Data Salah")
    except:
        print("Terjadi sebuah kesalahan")

    buatBacaCsvPandas()   
