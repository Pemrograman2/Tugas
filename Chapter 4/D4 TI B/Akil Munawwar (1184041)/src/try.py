# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 22:29:11 2019

@author: Asus
"""

#Fungsi Try Except 
def TryCsvPandas():
    try:
        rd = pandas.read_csv('try.csv')
        print(r)
    except SyntaxError:
        print("Syntax nya salah...")
    except NameError:
        print("Variabel tidak sesuai...")
    except TypeError:
        print("Tipe data nya salah....")
    except:
        print("Teliti lah anjer...")

TryCsvPandas()