# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 21:06:46 2019

@author: NISA
"""

#Menulis File CSV dengan fungsi to_csv dengan library pandas
import pandas

df = pandas.read_csv('Teori1.csv')
df.to_csv('Teori4.csv')