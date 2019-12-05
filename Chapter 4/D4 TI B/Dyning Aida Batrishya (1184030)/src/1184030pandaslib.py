import pandas

def openlistmodepandas():
    df = pandas.read_csv('1184030.csv')
    print(df)

def opendictmodepandas():
    df = pandas.read_csv('1184030.csv')
    dt = pandas.DataFrame.from_dict(df)
    print(dt)