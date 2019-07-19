import pandas as pd
import numpy as np

from quant import Quant

class Volatility(Quant):
    def __init__(self, path, resolution):
        super(Volatility, self).__init__(path, resolution)
        self.drop_origin_cols()

    def volatility_rank_hour(self):
        return self.df \
            .pivot_table(index='hour',
                         columns='volatility_rank',
                         values='DateTime',
                         aggfunc=np.size)

    def volatility_rank_weekday(self):
        return self.df \
            .pivot_table(index='weekday',
                         columns='volatility_rank',
                         values='DateTime',
                         aggfunc=np.size)



if __name__ == '__main__':
    v = Volatility(path=r'../data/EURUSD_Hourly.csv', resolution='H')
    v.insert(name='volatility', func=lambda:abs(v.df['mid_High']-v.df['mid_Close']), rank=True)
    # print(v.volatility_rank_hour())
    print(v.volatility_rank_weekday())




