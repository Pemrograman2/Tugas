#Fungsi Try Except 
def readCsvPandas():
    try:
        rd = pandas.read_csv('Data.csv')
        print(r)
    except SyntaxError:
        print("Kesalahan penulisan syntax")
    except NameError:
        print("Tidak ditemukan Variabel yang sesuai")
    except TypeError:
        print("Tipe data yang dimasukkan salah")
    except:
        print("Terdapat Kesalahan, Coba lebih teliti")

readCsvPandas()
