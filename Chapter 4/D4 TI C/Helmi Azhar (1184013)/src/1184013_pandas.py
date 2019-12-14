# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 23:11:15 2019

@author: Asus
"""

def listPandas():
   python_file = pandas.read_csv('mhs.csv')
   kobra_list1 = python_file.values
   kobra_list2 = list(python_file.head())

    print(kobra_list1)
		print(kobra_list2)

def dictPandas():
    python_file = pandas.read_csv('mhs.csv').to_dict()

    print(python_file)

def changeDatetime():
    python_file = pandas.read_csv('mhs.csv')

    python_file["date"] = pandas.to_datetime(python_file["date"])

def reindex():
    python_file = pandas.read_csv('mhs.csv')

    kobra_index = ['1', '2', '0']

    python_file.reindex(eta_index)

def renameColumn():
    python_file = pandas.read_csv('mhs.csv')

    kisi = python_file.rename(columns={"Npm": "npm"})

    print(kisi)
	
def writePandas():
    buat_data = pandas.DataFrame({'Nama': ['IwanPales', 'Mariong'],
                                  'Absen': ['6', '9']})
    buat_data.to_csv('file_pandas.csv', index=False)

def openPandas():
    baca_data = pandas.read_csv('file_pandas.csv')

    print(baca_data)