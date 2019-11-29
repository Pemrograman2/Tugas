import pandas

#No. 3
def listPandas():
    df = pandas.read_csv('contoh.csv')
    print(df)

#No. 4
def dictPandas():
    df = pandas.read_csv('contoh.csv')
    dt = pandas.DataFrame.from_dict(df)
    print(dt)
    
# No. 5
def ubahTanggal():
    df = pandas.read_csv('contoh.csv', parse_dates=['NPM'])
    print(df)

#No. 6
def ubahIndexKolom():
    df = pandas.read_csv('contoh.csv')
    df.index = ['Row_1', 'Row_2']
    print(df)

#No. 7
def ubahNamaKolom():
    df = pandas.read_csv('contoh1.csv')
    df.columns =['Col_1', 'Col_2'] 
    print(df)


def errorPandas(): 
    try:
    df = pandas.read_csv( 'contoh1.csv' ) 
        print ( dt ) 
    except: 
        print ("Eror")


        
def tulisPandas():
    df = pandas.read_csv('contoh1.csv', 
            index_col='no', 
            parse_dates=['NPM'],
            header=0, 
            names=['no', 'nama', 'NPM'])
    df.to_csv('contoh1.csv')
    