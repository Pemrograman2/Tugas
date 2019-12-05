# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 20:47:59 2019

@author: Putri Nella
"""

#Menulis File CSV dengan fungsi to_csv dengan library pandas
import pandas

df = pandas.read_csv('Teori1.csv')
df.to_csv('Teori4.csv')