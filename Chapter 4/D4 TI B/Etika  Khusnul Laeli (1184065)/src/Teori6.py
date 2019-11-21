# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 19:52:42 2019

@author: ANIF
"""

#Menulis File CSV dengan fungsi to_csv dengan library pandas
import pandas

df = pandas.read_csv('Teori1.csv')
df.to_csv('Teori4.csv')