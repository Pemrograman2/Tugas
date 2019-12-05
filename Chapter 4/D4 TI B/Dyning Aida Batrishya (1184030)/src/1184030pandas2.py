import pandas


def opendictmodepandas():
    df = pandas.read_csv('1184030.csv')
    dt = pandas.DataFrame.from_dict(df)
    print(dt)
