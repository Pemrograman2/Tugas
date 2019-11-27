import csv

#No1
def ListModeCSV():
    with open('Pemrograman2.csv') as csvfile:
        readCSV = csv.read(csvfile, delimiter=',')
        for row in readCSV:
            print(row[0], row[1], row[2])


#No2            
def CSVDIctmode():
    with open('tgs.csv', mode='r') as csvfile:
        readCSV = csv.DictReader(csvfile)
        for row in readCSV:
            print(row['npm'], row['nama'], row['kelas'])

def CSVWrite():
    with open('tgs2.csv', mode='w') as csvfile:
        fieldnames = ['npm', 'nama', 'kelas', 'Jurusan']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
        writer.writeheader()
        writer.writerow({'npm': '1184024', 'nama': 'Syabriena', 'kelas': 'D4TI2B', 'Jurusan': 'TI'})
        writer.writerow({'npm': '1184021', 'nama': 'Putri', 'kelas': 'D4TI2B', 'Jurusan': 'MI'})

def writeCSV():
    with open('tgs2.csv', mode='w') as csvfile:
        fieldnames = ['npm', 'nama', 'kelas', 'tanggal lahir']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
        writer.writeheader()
        writer.writerow({'npm': '1184024', 'nama': 'Syabriena', 'kelas': 'D4TI2B', 'tanggal lahir': '24/06/1999'})
        writer.writerow({'npm': '1184021', 'nama': 'Putri', 'kelas': 'D4TI2B', 'tanggal lahir': '21/07/2005'})