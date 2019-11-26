# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 21:49:45 2019

@author: Asus
"""

import csv

#no 1
def ModeListCSV():
    with open ('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[0], row[1], row[2])

#no 2
def ModeDictCSV():
    with open ('data.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['nama'], row['kelas'],row['nilai'])