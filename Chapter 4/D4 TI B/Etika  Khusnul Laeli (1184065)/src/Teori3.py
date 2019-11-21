# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 22:47:58 2019

@author: ANIF
"""

#Menulis file CSV dengan fungsi DictWriter dengan library CSV
import csv

with open('Teori3.csv', mode='w') as csv_file:
    fieldnames = ['npm', 'nama', 'kelas']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({'npm': '11840033', 'nama': 'Lentera Rizqia', 'kelas':'D4TI2B'})
    writer.writerow({'npm': '11840044', 'nama': 'Annassyaf', 'kelas':'D4TI2B'})
    
