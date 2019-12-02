import csv

with open('jurusan', mode='w') as csv_file:
     fieldnames=['npm','nama']
     writer=csv.DictWriter(csv_file,fieldnames=fieldnames)


     writer.writeheader()
     writer.writerow({'npm':'1184095' , 'nama':'diy' })
     writer.writerow({'npm':'2184122' , 'nama':'dii' })
     
     