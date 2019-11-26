import pandas

def listPandas():
   batu_file = pandas.read_csv('vianmahasiswa.csv')
   pasir_list1 = batu_file.values
   pasir_list2 = list(batu_file.head())

    print(pasir_list1)
		print(pasir_list2)

def dictPandas():
    batu_file = pandas.read_csv('vianmahasiswa.csv').to_dict()

    print(batu_file)

def changeDatetime():
    batu_file = pandas.read_csv('vianmahasiswa.csv')

    batu_file["date"] = pandas.to_datetime(batu_file["date"])

def reindex():
    batu_file = pandas.read_csv('vianmahasiswa.csv')

    pasir_index = ['1', '2', '0']

    batu_file.reindex(eta_index)

def renameColumn():
    batu_file = pandas.read_csv('vianmahasiswa.csv')

    semen = batu_file.rename(columns={"Nama Mahasiswa": "name"})

    print(semen)
	
def writePandas():
    buat_data = pandas.DataFrame({'Nama Mahasiswa': ['vian', 'fina'],
                                  'kadarcinta': ['biasa', 'super']})
    buat_data.to_csv('pandas_file_uey.csv', index=False)

def openPandas():
    baca_data = pandas.read_csv('pandas_file_uey.csv')

    print(baca_data)