# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 15:10:55 2019

@author: USER
"""

import pandas

#soal3
def bukaModeListpandasa():
    dt = pandas.read_csv('data.csv')
    print(dt)
    
#soal4
def bukaModeDictPandas():
    df = pandas.read_csv('data.csv')
    dt = pandas.Dataframe.from_dict(df)
    print(dt)
    
#soal5
def ubahFromatTanggal():
    df = pandas.read_csv('data.csv', parse_dates=['tanggal lahir'])
    print(df)
    
#soal6
def  ubahIndexKolom():
    df = pandas.read_csv('data.csv')
    df.index = ['Row_1', 'Row_2']
    print(df)
    
#soal7
def ubahNamaKolom():
    df = pandas.read_csv('data.csv')
    df.columns =['col_1', 'col_2', 'col_3', 'col_4']
    print(df)
    
def tulisanCsvPandas():
    df = pandas.read_csv('data.csv',
            index_col='Npm',
            parse_dates=['tanggal lahit'],
            header=0,
            names=['Npm', 'Nama', 'kelas', 'tanggal lahir'])
    df.to_csv('data.csv')