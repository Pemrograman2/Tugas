import csv

with open('jurusan1', mode='w') as csv_file:
     fieldnames=['no','nama']
     writer=csv.DictWriter(csv_file,fieldnames=fieldnames)

     writer.writeheader()
     writer.writerow({'no':'1' , 'nama':'Djoee' })
     writer.writerow({'no':'2' , 'nama':'Noobies' })