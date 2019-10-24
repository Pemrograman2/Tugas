# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 21:04:07 2019

@author: lenovo
"""

npm=int(input("masukan npm anda : "))
TwoLastDigit=abs(npm)%100 # modulus menetukan ambil 2 digit terakhir
for i in range(TwoLastDigit):
    print("Halo, ", npm, " Apa kabar ?")