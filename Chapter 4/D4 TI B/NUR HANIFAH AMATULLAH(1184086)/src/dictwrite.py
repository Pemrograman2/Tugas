import csv

with open('Jurusan1', mode='w') as csv_file:
     fieldnames=['NPM','Nama']
     writer=csv.DictWriter(csv_file,fieldnames=fieldnames)

     writer.writeheader()
     writer.writerow({'NPM':'1184020' , 'Nama':'Dudu' })
     writer.writerow({'NPM':'1184030' , 'Nama':'Didi' })

