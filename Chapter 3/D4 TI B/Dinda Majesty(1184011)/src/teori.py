# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:28:53 2019

@author: trian
"""
#input output
print("masukkan nama anda : ")
nama = input()
print("nama saya adalah " + nama)

#perulangan while
hitung = 0
while (hitung < 9):
    print ('hitungan ke :', hitung)
    hitung = hitung + 1

print ("Good bye!")

#perulangan for
minum = ["kopi", "susu", "teh"]
for minuman in minum:
    print("Saya suka minum", minuman)

#nested loop
    i = 2
while(i < 100):
    j = 2
    while(j <= (i/j)):
        if not(i%j): break
        j = j + 1
    if (j > i/j) : print(i, " is prime")
    i = i + 1

print ("Good bye!")

#if statement
a = 330
b = 200
if a > a:
  print("a lebih besar dari b")

#elif
a = 33
b = 33
if b > a:
  print("b lebih besar dari a")
elif a == b:
  print("a sama dengan b")
  
#else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
#nested if
x = 41

if x > 10:
  print("lebih besar dari 10,")
  if x > 20:
    print("lebih besar dari 20!")
  else:
    print("tidak melebihi 20.")
    
#try except
try:
  print(x)
except NameError:
  print("Variable x tidak ada")
except:
  print("ada sesuatu yang salah nih")