import pandas as pd
from sklearn.linear_model import LogisticRegression as LR
from sklearn.model_selection import train_test_split
import statsmodels.api as sm


class Quant():
    def __init__(self, file, resolution):
        self.raw_df = pd.read_csv(file)
        self.raw_df.rename(columns={'last_Volume': 'volume'}, inplace=True)
        self.resolution = resolution
        self.df = self.add_mid(self.raw_df)
        self.split_dt()

    def split_dt(self):
        _dt = pd.to_datetime(self.df['DateTime'])
        self.df['date'] = _dt.dt.date
        self.df['weekday'] = _dt.dt.weekday
        self.df['hour'] = _dt.dt.hour
        self.df['minute'] = _dt.dt.minute
        self.df['second'] = _dt.dt.second

    def add_mid(self, df):
        col_names = list(df.columns)
        types = set([c.split("_")[1] for c in col_names if "_" in c])
        for t in types:
            df.insert(1, f'mid_{t}', (self.raw_df[f'bid_{t}']+self.raw_df[f'ask_{t}'])/2)
        return df

    def drop_origin_cols(self):
        cols_to_drop = set(self.df.columns)
        cols_to_drop = set([c for c in cols_to_drop if "_" in c and 'mid' not in c])
        self.df = self.df.drop(cols_to_drop, axis=1)

    def insert(self, name, func, rank=False):
        self.df[name] = func()
        if rank:
            rank_col_name = name +'_rank'
            self.df[rank_col_name] = pd.cut(self.df[name], 10, labels=range(1, 11))

    def lg_validation(self, x, y):
        x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8)
        x_train = x_train.values.reshape(-1, 1)
        y_train = y_train.get_values().reshape(-1, 1)
        model = LR()
        model.fit(x_train, y_train)

        x_test = x_test.values.reshape(-1, 1)
        y_test = y_test.get_values().reshape(-1, 1)
        print(model.score(x_test, y_test))

    def r_style_lg_validate(self, x, y):
        max_x = max(x.values)
        x = x/max_x
        y = pd.Series(y.get_values()/10, index=y.index)
        logit = sm.Logit(x, y)
        result = logit.fit()
        print(result.summary())





