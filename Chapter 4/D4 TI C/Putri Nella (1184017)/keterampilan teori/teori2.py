# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 20:44:04 2019

@author: Putri Nella
"""

#Menulis File CSV dengan Fungsi Writer dengan library CSV
import csv 

with open('Teori2.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow({'npm', 'nama', 'kelas'})
    csv_writer.writerow({'1184009', 'mami', 'D4TI2C'})
    csv_writer.writerow({'1184012', 'papi', 'D4TI2B]C'})