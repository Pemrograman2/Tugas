# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 18:35:12 2019

@author: Asus
"""

class Bakso:
    def __init__(self,bakso,mie):
        self.bakso=bakso
        self.mie=mie
    def masak(self):
        print("Makan : " + self.bakso)
        print("Pakai : " + self.mie)
        print()