# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 22:37:55 2019

@author: NISA
"""

#Menulis File CSV dengan Fungsi Writer dengan library CSV
import csv 

with open('Teori2.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow({'npm', 'nama', 'kelas'})
    csv_writer.writerow({'1184008', 'Gany Berdu Sura', 'D4TI2C'})
    csv_writer.writerow({'1184095', 'Dian Markuci', 'D4TI2B]C'})