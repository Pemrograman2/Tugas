#Membaca File CSV dengan Fungsi DictReader dengan Library CSV
import csv

with open('CSV1.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row['NPM'], row['NAMA'], row['JURUSAN'])