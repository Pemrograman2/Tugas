import csv

with open ('infor.csv', mode='w') as csv_file:
    judulkolom = ['NPM', 'Nama', 'Kelas', 'Jurusan']
    writer = csv.DictWriter(csv_file, fieldnames=judulkolom)

    writer.writeheader()
    writer.writerow({'NPM': '1184099', 'Nama': 'iwan', 'Kelas': '1a', 'jurusan': 'TI'})
    writer.writerow({'NPM': '1184098', 'Nama': 'budi', 'Kelas': '1b', 'jurusan': 'LB'})
    writer.writerow({'NPM': '1184097', 'Nama': 'wati', 'Kelas': '1c', 'jurusan': 'MI'})