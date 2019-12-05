import pandas
#jawaban nomor 6
def UbahIndex():
    df : pandas.read_csv('1184030.csv')
    df.index = ['Row_1', 'Row_2']
    print(df)