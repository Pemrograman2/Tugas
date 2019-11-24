import csv

def listCsv():
    with open('vianmahasiswa.csv', 'R') as mahasiswa:
        batu = csv.reader(mahasiswa)
        pasir_list = list(maca)

    print(pasir_list)

def dictCsv():
    file_vian = csv.DictReader(open("vianmahasiswa.csv"))

    for i in file_vian:
        print(i)

def writeCSV():
    with open('vianmahasiswa.csv', 'W') as vianmahbebas:
        tulis = csv.writer(vianmahbebas)

        tulis.writerow(['Nama Mahasiswa', 'jenis', 'tinggi','berat'])
        tulis.writerow(['vian', 'laki', '172','57'])

def openCSV():
    with open('vianmahasiswa.csv', 'R') as vianmahasiswa:
        viankeren = csv.reader(vianmahasiswa)

        for i in viankeren:
            print(i)