import csv

with open('contoh.csv',mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row['no'], row['nama'], row['jurusan'])