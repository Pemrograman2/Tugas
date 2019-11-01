npm = input ("Masukan NPM Anda: ")

nPm = npm[-3:]

b = 0

for i in nPm:
    c = int(i) + b
    b = c
    
for i in range(b):
    print ("Hallo, "+ nPm + "Apa Kabar?")