import csv

def listCsv():
    with open('terlaluganteng.csv', 'r') as ganteng:
        maca = csv.reader(ganteng)
        eta_list = list(maca)

    print(eta_list)

def dictCsv():
    file_ganteng = csv.DictReader(open("terlaluganteng.csv"))

    for i in file_ganteng:
        print(i)

def writeCSV():
    with open('anggaemangganteng.csv', 'w') as gantengsekali:
        tulis = csv.writer(gantengsekali)

        tulis.writerow(['nama', 'pekerjaan', 'tingkat kegantengan'])
        tulis.writerow(['angga', 'mahasiswa', 'maksimal'])

def openCSV():
    with open('anggaemangganteng.csv', 'r') as terlalugnteng:
        gantengih = csv.reader(terlalugnteng)

        for i in gantengih:
            print(i)