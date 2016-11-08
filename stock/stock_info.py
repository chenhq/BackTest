import pandas as pd


class StockInfo:

    base_dir = "/data/tdb/data"
    stock_info_dir = base_dir + "/stock_info/"

    def __init__(self, filename='all_tickers.csv'):
        try:
            df = pd.read_csv(self.__class__.kline_1day_dir + filename)
            self.data = df[['secID', 'ticker', 'exchangeCD', 'secShortName', 'listStatusCD', 'listDate']]
        except Exception as e:
            print(e)
            self.data = pd.DataFrame()

    def data(self):
        return self.data

    def price_filter(self, min_price=0, max_price=1000):
        pass

    def flo_filter(self, min_flo=10**8, max_flo=10**10):
        pass

    def list_date_filter(self, start_date='19900101', end_date='20500101'):
        pass
