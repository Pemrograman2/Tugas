# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 20:52:15 2019

@author: NISA
"""

#Menulis file CSV dengan fungsi DictWriter dengan library CSV
import csv

with open('Teori3.csv', mode='w') as csv_file:
    fieldnames = ['npm', 'nama', 'kelas']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({'npm': '1184038', 'nama': 'Nurul Kamila', 'kelas':'D4TI2C'})
    writer.writerow({'npm': '1184017', 'nama': 'Putri Nella', 'kelas':'D4TI2C'})