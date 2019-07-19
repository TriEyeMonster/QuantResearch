import pandas as pd


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


