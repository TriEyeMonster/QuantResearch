import pandas as pd
import numpy as np

from quant import Quant

class Volatility(Quant):
    def __init__(self, path, resolution):
        super(Volatility, self).__init__(path, resolution)
        self.drop_origin_cols()

    def most_volatility_hour(self):
        self.df['volatility'] = abs(self.df['mid_High']-self.df['mid_Close'])
        self.df['vola_rank'] = pd.cut(self.df['volatility'], 10, labels=[0,1,2,3,4,5,6,7,8,9])
        self.df = self.df.sort_values(by=['rank'], ascending=False)
        pass


if __name__ == '__main__':
    v = Volatility(path=r'../data/EURUSD_Hourly.csv', resolution='H')
    v.most_volatility_hour()




