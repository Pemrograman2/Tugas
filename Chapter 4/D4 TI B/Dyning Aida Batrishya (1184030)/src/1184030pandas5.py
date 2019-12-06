import pandas

#jawaban nomor 7
def UbahNamaKolom():
    ubah = pandas.read_csv('1184030.csv')
    ubah.columns = ['Col_1','Col_2','Col_3','Col_4']
    print(ubah)