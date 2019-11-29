import csv

with open('contoh', mode='w') as csv_file:
     fieldnames=['no','nama']
     writer=csv.DictWriter(csv_file,fieldnames=fieldnames)

     writer.writeheader()
     writer.writerow({'no':'3' , 'nama':'pute' })
     writer.writerow({'no':'8' , 'nama':'bintang' })