import csv

with open('jurusan', mode='w') as csv_file:
     fieldnames=['npm','nama']
     writer=csv.DictWriter(csv_file,fieldnames=fieldnames)

     writer.writeheader()
     writer.writerow({'npm':'1' , 'nama':'diy' })
     writer.writerow({'npm':'2' , 'nama':'dii' })