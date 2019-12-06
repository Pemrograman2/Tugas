# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 18:38:00 2019

@author: USER
"""

npm=int(input("masukan npm anda : "))
TwoLastDigit=abs(npm)%100 # modulus menetukan ambil 2 digit terakhir
for i in range(TwoLastDigit):
    print("Halo, ", npm, " Apa kabar ?")