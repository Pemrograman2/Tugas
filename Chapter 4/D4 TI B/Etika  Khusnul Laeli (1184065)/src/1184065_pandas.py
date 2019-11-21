# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 19:02:58 2019

@author: ANIF
"""

import pandas

#Jawaban No.3
def MembukaModeListPandas():
    df = pandas.read_csv('Teori1.csv')
    print(df)
    
#Jawaban No.4
def MembukaModeDictPandas():
    df = pandas.read_csv('Teori1.csv')
    dt = pandas.DataFrame.from_dict(df)
    print(dt)
    
#Jawaban No.5
def merubahFormatTanggal():
    df = pandas.read_csv('Teori1.csv', parse_dates=['tanggal lahir'])
    print(df)

#Jawaban No.6
def merubahIndexKolom():
    df = pandas.read_csv('Teori1.csv')
    df.index = ['Row_1', 'Row_2']
    print(df)
    
#Jawababn No.7
def merubahNamaKolom():
    df = pandas.read_csv('Teori1.csv')
    df.columns =  ['Co1_1', 'Co1_2', 'Co1_3', 'Co1_4']
    print(df)

def tulisCsvPandas():
    df = pandas.read_csv('Teori1.csv',
                         index_col='NPM',
                         parse_dates=['Tanggal lahir'],
                         header=0,
                         names=['NPM', 'Nama', 'Kelas','Tanggal lahir'])
    df.to_csv('teori5.csv')

    