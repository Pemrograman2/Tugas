import csv

with open('contoh', mode='w') as csv_file:
     csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
     csv_writer.writerow(['no' , 'nama' , 'npm' ])
     csv_writer.writerow(['1' , 'pute' , '1184004' ])
     csv_writer.writerow(['2' , 'bintang' , '1184020' ])