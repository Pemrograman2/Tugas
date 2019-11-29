import csv

with open('Jurusan1', mode='w') as csv_file:
     csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
     csv_writer.writerow(['NPM' , 'Nama' , 'Jurusan' ])
     csv_writer.writerow(['1184020' , 'Dudu' , 'TI' ])
     csv_writer.writerow(['1184030' , 'Didi' , 'LB' ])

