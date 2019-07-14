import pandas as pd


class Quant():
    def __init__(self, file, resolution):
        self.raw_df = pd.read_csv(file)
        self.raw_df.rename(columns={'last_Volume': 'volume'}, inplace=True)
        self.resolution = resolution
        self.df = self.add_mid(self.raw_df)
        # Todo: split datetime column to date and hour

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
