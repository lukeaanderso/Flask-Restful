__author__ = 'landerson'

from pandas.io.data import DataReader


def get_yahoo(symbol, date, field):
    f = DataReader(symbol.upper(), 'yahoo', date, date)
    f.columns = [c.lower() for c in f.columns]
    data = f.ix[date][field]
    return data

