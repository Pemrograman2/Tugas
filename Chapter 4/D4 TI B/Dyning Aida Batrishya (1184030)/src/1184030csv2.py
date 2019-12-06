import csv

def openmodedict():
    with open('1184030.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['npm'], row['namalengkap'], row['kelas'])