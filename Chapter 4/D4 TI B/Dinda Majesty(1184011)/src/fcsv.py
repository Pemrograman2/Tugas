#CSV Reader
import csv

with open('FCSV.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)

#CSV Writer
import csv

with open('asal.csv', mode='w') as csvfile:
    fieldnames = ['nomor', 'nama klub', 'jumlah main', 'poin']
    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    csv_writer.writeheader()
    csv_writer.writerow({'nomor': '1', 'nama klub': 'Asal-Asalan', 'jumlah main': '8','poin': '10'})
    csv_writer.writerow({'nomor': '2', 'nama klub': 'Asal-Asalan2', 'jumlah main': '8','poin': '12'})

import pandas as pd
df1=pd.read_csv("FCSV.csv")
print(df1)

import pandas as pds
df2=pds.read_excel("FCSV.xlsx", index_col=None, header=None)
print(df2)