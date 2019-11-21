# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 21:10:05 2019

@author: ANIF
"""

#Membaca File CSV dengan fungsi reader dengan library CSV
import csv 

with open('Teori1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row[0], row[1], row[2])