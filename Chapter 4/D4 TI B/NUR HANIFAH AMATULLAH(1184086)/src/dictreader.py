import csv

with open('Book1.csv',mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row['NPM'], row['Nama'], row['Jurusan'])

