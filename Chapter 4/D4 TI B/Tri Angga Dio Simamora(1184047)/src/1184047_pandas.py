import pandas

def listPandas():
    maca_file = pandas.read_csv('terlaluganteng.csv')
    eta_list1 = maca_file.values
    eta_list2 = list(maca_file.head())

    print(eta_list1)
    print(eta_list2)

def dictPandas():
    maca_file = pandas.read_csv('terlaluganteng.csv').to_dict()

    print(maca_file)

def changeDatetime():
    maca_file = pandas.read_csv('terlaluganteng.csv')

    maca_file["date"] = pandas.to_datetime(maca_file["date"])

def reindex():
    maca_file = pandas.read_csv('terlaluganteng.csv')

    eta_index = ['1', '2', '0']

    maca_file.reindex(eta_index)

def renameColumn():
    maca_file = pandas.read_csv('terlaluganteng.csv')

    euweh = maca_file.rename(columns={"nama": "name"})

    print(euweh)