import pandas as pd
from datetime import datetime


class MarketData:
    """
    get market data: kline_1day, kline_1min, tick, order, order_queue, transaction
    """

    base_dir = "/data/tdb/data"
    base_info_dir = base_dir + "/base_info/"
    kline_1day_dir = base_dir + "/interday/kline_1day/"
    kline_1min_dir = base_dir + "/intraday/kline_1min/"
    tick_dir = base_dir + "/intraday/tick/"

    @classmethod
    def get_kline_1day(cls, stk, str_month):
        try:
            file = cls.kline_1day_dir + str_month + "/" + stk + ".csv"
            df = pd.read_csv(file, dtype={'code': str}, parse_dates=[1], index_col=[1])
            df.rename(columns={' open': 'open', ' high': 'high', ' low': 'low', ' close': 'close', ' volume': 'volume',
                               ' turnover': 'turnover'}, inplace=True)
            used_columns = ['code', 'open', 'high', 'low', 'close', 'volume', 'turnover']
            result = df[used_columns]
        except Exception as e:
            print(e)
            result = pd.DataFrame()
        return result

    @staticmethod
    def parse_datetime(str_date, str_time):
        try:
            year = int(str_date[:4])
            month = int(str_date[4:6])
            day = int(str_date[6:8])

            hour = int(str_time[:-7])
            minute = int(str_time[-7:-5])
            second = int(int(str_time[-5:]) / 100000)

            dt = datetime(year, month, day, hour, minute, second)
        except Exception as e:
            print(e)
            dt = datetime(1990, 1, 1, 0, 0, 0)
        return dt

    @classmethod
    def get_kline_1min(cls, stk, str_date):
        try:
            file = cls.kline_1min_dir + str_date + "/" + stk + ".csv"
            df = pd.read_csv(file, dtype={'code': str}, parse_dates={'datetime': [1, 2]},
                             date_parser=cls.parse_datetime, index_col='datetime')
            df.rename(columns={' open': 'open', ' high': 'high', ' low': 'low', ' close': 'close', ' volume': 'volume',
                               ' turnover': 'turnover'}, inplace=True)
            used_columns = ['code', 'open', 'high', 'low', 'close', 'volume', 'turnover']
            result = df[used_columns]
        except Exception as e:
            print(e)
            result = pd.DataFrame()
        return result

    @classmethod
    def get_tick(cls, stk, str_date):
        try:
            file = cls.tick_dir + str_date + "/" + stk + ".csv"
            df = pd.read_csv(file, parse_dates={'datetime': [1, 2]},
                             date_parser=cls.parse_datetime, index_col='datetime')
            df.rename(columns={'windcode': 'code'}, inplace=True)
            df['code'] = df['code'].map(lambda x: x[:6])
            result = df
        except Exception as e:
            print(e)
            result = pd.DataFrame()
        return result


    @classmethod
    def get_order(cls, stk, str_date):
        pass

    @classmethod
    def get_order_queue(cls, stk, str_date):
        pass

    @classmethod
    def get_transaction(cls, stk, str_date):
        pass
