import csv

def listCsv():
    with open('viankereneuy.csv', 'r') as mahasiswa:
        batu = csv.reader(mahasiswa)
        pasir_list = list(batu)

    print(pasir_list)

def dictCsv():
    file_vian = csv.DictReader(open("viankereneuy.csv"))

    for i in file_vian:
        print(i)

def writeCSV():
    with open('viankereneuy.csv', 'w') as vianmahbebas:
        tulis = csv.writer(vianmahbebas)

        tulis.writerow(['Nama Mahasiswa', 'pendidikan', 'berat'])
        tulis.writerow(['vian', 'D4', 'kali'])

def openCSV():
    with open('viankereneuy.csv', 'r') as vianmahasiswa:
        viankeren = csv.reader(vianmahasiswa)

        for i in viankeren:
            print(i)