from market.market_data import MarketData as md
from stock.stock_info import StockInfo as si


def get_all_tickers():
    return si.data


def ma_20_calculate():
    month09 = md.get_kline_1day(stk='000001', str_month='201609')
    month10 = md.get_kline_1day(stk='000001', str_month='201609')
