import pandas as pd

from quant import Quant

class Volatility(Quant):
    def __init__(self, path, resolution):
        super(Volatility, self).__init__(path, resolution)
        self.drop_origin_cols()

    def most_volatility_hour(self):
        self.df = pd.cut(abs(self.df['mid_Close']-self.df['mid_Open']), 10)
        pass


if __name__ == '__main__':
    v = Volatility(path=r'../data/EURUSD_Hourly.csv', resolution='H')
    v.most_volatility_hour()




