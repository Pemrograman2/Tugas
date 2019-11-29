import csv

with open('Book1.csv') as csv_file:
    csv_reader = csv.reader(csv_file , delimiter=',')
    for row in csv_reader:
        print(row)
