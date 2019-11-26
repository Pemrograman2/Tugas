import pandas
def bukaModeDictPandas():
    df = pandas.read_csv('praktikum 1.csv')
    dt = pandas.DataFrame.from_dict(df)
    print(dt)
    