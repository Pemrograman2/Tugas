import csv

with open ('excsv.csv', mode='w') as csvfile:
    judulkolom = ['NPM', 'Nama', 'Kelas', 'Jurusan']
    writer = csv.DictWriter(csvfile, fieldnames=judulkolom)

    writer.writeheader()
    writer.writerow({'NPM': '1184099', 'Nama': 'syabriena', 'Kelas': '1a', 'jurusan': 'TI'})
    writer.writerow({'NPM': '1184098', 'Nama': 'putri', 'Kelas': '1b', 'jurusan': 'LB'})
    writer.writerow({'NPM': '1184097', 'Nama': 'veriane', 'Kelas': '1c', 'jurusan': 'MI'})