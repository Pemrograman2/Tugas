#from csv import reader
#import csv

#with open('1184030.csv', 'r') as csv_file : 
#    csv_reader = csv.reader(csv_file, delimiter=';')
    #line_c = 0
#    for row in csv_reader :
#        print(row)
        #print(f'\t Mahasiswa ini memiliki NPM {row[0]}, Bernama {row[1]}, Berada di kelas{row[2]}.')
        #if line_c == 0:
        #    print(f' {", ".join(row)}')
        #   line_c += 1
        #else:
        #    print(f'\t Mahasiswa ini memiliki NPM {row[0]}, Bernama {row[1]}, Berada di kelas{row[2]}.')
        #    line_c += 1

import csv

with open('1184030.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            line_count += 1
    print(f'Processed {line_count} lines.')