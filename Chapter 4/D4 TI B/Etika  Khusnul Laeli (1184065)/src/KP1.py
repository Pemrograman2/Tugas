# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 00:19:25 2019

@author: ANIF
"""

#Jawaban No.1
def MembukaModeListCsv():
    with open('Teori1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[0], row[1], row[2])