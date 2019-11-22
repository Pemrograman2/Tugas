import pandas

def pandasList():
    pd = pandas.read_csv("FCSV.csv")
    print(pd)

def pandasDict():
    pds = pandas.read_csv("dictionary.csv")
    crot = pandas.DataFrame.from_dict(pds)
    print(crot)

def Tanggal():
    tanggal = pandas.read_csv("FCSV.csv")
    tanggal['tanggal']=pandas.to_datetime(tanggal['tanggal'])
    print(tanggal)

def ubahIndex():
    baris = pandas.read_csv("FCSV.csv")
    barisindex = ['1','2', '0', '3', '5', '4','6', '7', '9', '8']
    oke = baris.reindex(barisindex)
    print(oke)

def ubahColumn():
    ubah = pandas.read_csv("FCSV.csv")
    okey = ubah.rename(columns={"nomor" : "number"})
    print(okey)

