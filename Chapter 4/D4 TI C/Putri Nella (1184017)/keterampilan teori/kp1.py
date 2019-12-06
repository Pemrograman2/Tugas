# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 20:35:52 2019

@author: Putri Nella
"""

#No.1
def MembukaModeListCsv():
    with open('Teori1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[0], row[1], row[2])