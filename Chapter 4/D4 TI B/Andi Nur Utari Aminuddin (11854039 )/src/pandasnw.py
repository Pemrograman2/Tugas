# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 23:48:55 2019

@author: Lenovo
"""
#Penggunaan Fungsi-Fungsi Format Pandas    
#Membaca File CSV dengan Fungsi read_csv dengan Library Pandas
import pandas

df = pandas.read_csv('teori1.csv')
print(df)

#Menulis File CSV dengan Fungsi to_csv dengan Library Pandas
import pandas

df = pandas.read_csv('teori1.csv')
df.to_csv('teori5.csv')