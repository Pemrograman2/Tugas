import pandas
def readcsvpandas():
    try:
        df = pandas.read_csv('1184030.csv')
        print(df)
    except Exception as e :
        print(e)