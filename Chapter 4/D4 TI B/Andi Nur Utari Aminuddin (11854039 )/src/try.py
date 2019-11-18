# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 00:26:27 2019

@author: Lenovo
"""

#Fungsi Try Except 
def readCsvPandas():
    try:
        rd = pandas.read_csv('teori1.csv')
        print(r)
    except SyntaxError:
        print("Kesalahan penulisan syntax")
    except NameError:
        print("Tidak ditemukan Variabel yang sesuai")
    except TypeError:
        print("Tipe data yang dimasukkan salah")
    except:
        print("Terdapat Kesalahan, Coba lebih teliti")

readCsvPandas()
