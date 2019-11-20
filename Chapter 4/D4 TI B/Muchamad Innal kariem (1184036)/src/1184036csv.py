

import csv

#Jawaban No. 1
def bukaModeListCsv():
    with open('jwb1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[0], row[1], row[2]) 

#Jawaban No. 2            
def bukaModeDictCsv():
    with open('jwb1.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['npm'], row['nama'], row['kelas'])

def tulisCsv():
    with open('teori.csv', mode='w') as csv_file:
        fieldnames = ['npm', 'nama', 'kelas', 'tanggal lahir']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writeheader()
        writer.writerow({'npm': '1184036', 'nama': 'Innal', 'kelas': 'D4TI2B', 'tanggal lahir': '03/11/2000'})
        writer.writerow({'npm': '1184222', 'nama': 'Apliriano', 'kelas': 'D4TI2J', 'tanggal lahir': '01/01/2001'})
