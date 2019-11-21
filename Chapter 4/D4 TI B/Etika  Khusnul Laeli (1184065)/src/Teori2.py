# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 21:23:24 2019

@author: ANIF
"""

#Menulis File CSV dengan Fungsi Writer dengan library CSV
import csv 

with open('Teori2.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow({'npm', 'nama', 'kelas'})
    csv_writer.writerow({'11840165', 'Rasya Athaya', 'D4TI2C'})
    csv_writer.writerow({'11840130', 'Khusnul Laeli', 'D4TI2B'})