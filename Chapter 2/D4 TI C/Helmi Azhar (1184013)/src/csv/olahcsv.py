#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 07:45:30 2019

@author: awangga
"""
import csv

with open('karyawanbaru.csv', mode='w') as csv_file:
    judulkolom = ['emp_name', 'dept', 'birth_month']
    writer = csv.DictWriter(csv_file, fieldnames=judulkolom)

    writer.writeheader()
    writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
    writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})
    writer.writerow({'emp_name': 'Lutfi', 'dept': 'IT', 'birth_month': 'Januari'})