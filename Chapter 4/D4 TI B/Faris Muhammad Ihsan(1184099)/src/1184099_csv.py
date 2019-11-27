import csv

#No1
def ListModeCSV():
    with open('Pemrograman2.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print(row[0], row[1], row[2])


#No2            
def CSVDIctmode():
    with open('tgs.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row['npm'], row['nama'], row['kelas'])

def CSVWrite():
    with open('tgs2.csv', mode='w') as csv_file:
        fieldnames = ['npm', 'nama', 'kelas', 'Jurusan']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writeheader()
        writer.writerow({'npm': '1184012', 'nama': 'Iwan', 'kelas': 'D4TI2B', 'Jurusan': 'TI'})
        writer.writerow({'npm': '1184013', 'nama': 'Budi', 'kelas': 'D4TI2B', 'Jurusan': 'LB'})

def writeCSV():
    with open('tgs2.csv', mode='w') as csv_file:
        fieldnames = ['npm', 'nama', 'kelas', 'tanggal lahir']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
        writer.writeheader()
        writer.writerow({'npm': '1184012', 'nama': 'Iwan', 'kelas': 'D4TI2B', 'tanggal lahir': '29/06/1977'})
        writer.writerow({'npm': '1184013', 'nama': 'Budi', 'kelas': 'D4TI2B', 'tanggal lahir': '13/02/1997'})