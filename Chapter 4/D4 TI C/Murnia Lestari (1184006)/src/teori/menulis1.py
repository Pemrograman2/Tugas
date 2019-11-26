#Menulis File CSV dengan Fungsi DictWriter dengan library CSV
import csv

with open('praktikum 3.csv', mode='w') as csv_file:
    fieldnames = ['NPM', 'NAMA', 'MATAKULIAH']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'NPM': '11840O6', 'NAMA': 'MURNIA LESTARI', 'MATAKULIAH': 'PEMROGRAMAN 2'})
    writer.writerow({'NPM': '1184038', 'NAMA': 'NURUL KAMILA'       , 'MATAKULIAH': 'PEMROGRAMAN 2'})