# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 22:02:13 2019

@author: Asus
"""

import pandas

#No. 3
def ModeListPandas():
    df = pandas.read_csv('data.csv')
    print(df)
    
#No 4
def ModeDictPandas():
    df = pandas.read_csv('data.csv')
    dt = pandas.DataFrame.from_dict(df)
    print(dt)
    
#No 5
def FormatNilai():
    df = pandas.read_csv('data.csv', parse_dates=['nilai'])
    print(df)

#No 6
def IndexKolom():
    df = pandas.read_csv('data.csv')
    df.index = ['1','2','3']
    print(df)
    
#No 7
def NamaKolom():
    df = pandas.read_csv('data.csv')
    df.columns =['Nama', 'Kelas', 'Nilai'] 
    print(df)