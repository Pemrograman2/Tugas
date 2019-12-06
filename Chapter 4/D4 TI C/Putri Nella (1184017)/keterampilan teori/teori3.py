# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 20:45:12 2019

@author: Putri Nella
"""

#Menulis file CSV dengan fungsi DictWriter dengan library CSV
import csv

with open('Teori3.csv', mode='w') as csv_file:
    fieldnames = ['npm', 'nama', 'kelas']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({'npm': '1184000', 'nama': 'pop', 'kelas':'D4TI2C'})
    writer.writerow({'npm': '1184076', 'nama': 'kok ', 'kelas':'D4TI2C'})