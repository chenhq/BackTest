import pandas as pd
from market.market_data import MarketData as md
from stock.stock_info import StockInfo


def stks_info_calculate(months, start_date='20000101', end_date='20500101'):
    stks_info = StockInfo()
    stks = stks_info.list_date_filter(end_date='20151001').get_data()
    stks_result = pd.DataFrame()

    for stk in stks['ticker']:
        all_read_datas = pd.DataFrame()
        try:
            for month in months:
                month_data = md.get_kline_1day(stk=stk, str_month=month)
                all_read_datas = pd.concat([all_read_datas, month_data])
        except Exception as e:
            pass
        if len(all_read_datas) > 0:
            all_read_datas['turnover_10day_mean'] = all_read_datas['turnover'].rolling(10).mean().shift(1)
            all_read_datas['turnover_1day'] = all_read_datas['turnover'].shift(1)

            all_read_datas['ma5'] = all_read_datas['close'].rolling(5).mean().shift(1)
            all_read_datas['ma10'] = all_read_datas['close'].rolling(10).mean().shift(1)
            all_read_datas['ma20'] = all_read_datas['close'].rolling(20).mean().shift(1)
            all_read_datas['ma60'] = all_read_datas['close'].rolling(60).mean().shift(1)

            stk_result = all_read_datas[start_date:end_date]
            stks_result = pd.concat([stks_result, stk_result])
    return stks_result

