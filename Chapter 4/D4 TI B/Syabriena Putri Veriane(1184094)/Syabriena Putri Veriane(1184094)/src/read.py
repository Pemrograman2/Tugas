#Read
import csv

with open('excsv.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row[0], row[1], row[3], row[4])