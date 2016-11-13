import pandas as pd


class StockInfo:

    base_dir = "/data/tdb/data"
    stock_info_dir = base_dir + "/stock_info/"

    def __init__(self, filename='all_tickers.csv'):
        try:
            df = pd.read_csv(self.__class__.stock_info_dir + filename)
            self.data = df[['secID', 'ticker', 'exchangeCD', 'secShortName', 'listStatusCD', 'listDate']]
        except Exception as e:
            print(e)
            self.data = pd.DataFrame()

    def get_data(self):
        return self.data

    def price_filter(self, min_price=0, max_price=1000):
        pass

    def flo_filter(self, min_flo=10**8, max_flo=10**10):
        pass

    def list_date_filter(self, start_date='19900101', end_date='20500101'):
        cond = (self.data['listDate'] > start_date) & (self.data['listDate'] < end_date)
        self.data = self.data.ix[cond,]
        return  self

