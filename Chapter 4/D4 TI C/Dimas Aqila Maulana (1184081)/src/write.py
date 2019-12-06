import csv

with open('jurusan1', mode='w') as csv_file:
     csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
     csv_writer.writerow(['no' , 'nama' , 'jurusan' ])
     csv_writer.writerow(['1' , 'april' , 'LB' ])
     csv_writer.writerow(['2' , 'oca' , 'MB' ])