import csv

with open('jurusan1', mode='w') as csv_file:
     csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
     csv_writer.writerow(['npm' , 'nama' , 'jurusan' ])
     csv_writer.writerow(['1184128' , 'Tata' , 'TI' ])
     csv_writer.writerow(['2184032' , 'Dadang' , 'MI' ])
     
     