import csv


def returnArduino():
    with open('hasil_data.csv', 'r') as waduwek:
        wekwek = csv.reader(waduwek)

        daftar=[]
        for i in wekwek:
            daftar.append(i)
    abc = daftar[1]

    return abc

def printData(data):
    print(data)