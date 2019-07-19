import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression as LR
# from sklearn.linear_model import RandomizedLogisticRegression as RLR

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

    def vola_x_volume(self):
        self.df = self.df.sort_values(by=['DateTime'], ascending=True) \
            .assign(shift_vola=self.df.volatility.shift(-1)) \
            .assign(vola_ratio=self.df.volatility/abs(self.df.mid_Close - self.df.mid_Open)) \
            .assign(vola_x_volume=lambda x: x.vola_ratio*x.volume) \
            .assign(shift_3_vxv= lambda x:
        (x.volume+x.volume.shift(1)+x.volume.shift(2))/
        ((x.volatility+x.volatility.shift(1)+x.volatility.shift(2))
         /(abs(x.mid_Close - x.mid_Open) +
           abs(x.mid_Close.shift(1) - x.mid_Open.shift(1)) +
           abs(x.mid_Close.shift(2) - x.mid_Open.shift(2)))))



if __name__ == '__main__':
    v = Volatility(path=r'../data/EURUSD_Hourly.csv', resolution='H')
    v.insert(name='volatility', func=lambda:abs(v.df['mid_High']-v.df['mid_Close']), rank=True)
    # print(v.volatility_rank_hour())
    # print(v.volatility_rank_weekday())
    v.vola_x_volume()
    v.df.to_csv(r'../data/EURUSD_H_VxV.csv')

    pass




