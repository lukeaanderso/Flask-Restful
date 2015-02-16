__author__ = 'landerson'

import datetime as dt
import pickle as pickle

from requests import put

from api._logging import logger
from api.trading import trade, brokers


def get_close(symbol, date):
    url = 'http://localhost:5000/'
    data = {'symbol': symbol.upper(),
            'date': date,
            'field': 'close'}
    for k, v in data.iteritems():
        msg = 'Sending {} : {}'.format(k, v)
        logger.info(msg)
    resp = put(url + 'data/', data=data)
    status = resp.status_code
    if status == 200:
        res = resp.json()
        return res['result']
    else:
        raise Exception('Data not found')


def send_trades(trade_list):
    url = 'http://localhost:5000/'
    data = {'trade_list': pickle.dumps(trade_list)}
    for t in trade_list:
        logger.info('Sending Trade: {}'.format(t))
    resp = put(url + 'trade/', data=data)
    status = resp.status_code
    if status == 200:
        res = resp.json()
        return res
    else:
        raise Exception('Trades processed incorrectly')


logger.info('Testing Data API')
symbols = ['AAPL', 'BIIB', 'GS']

asof = dt.date(2014, 12, 31)
prices = [get_close(s, asof) for s in symbols]
shrs = [3, 5, 7]
logger.info(prices)

trade_list = [trade(account='GLOBALMN',
                    symbol=s,
                    shares=sh,
                    px=p,
                    broker=brokers.ms) for s, p, sh in zip(symbols, prices, shrs)]

trade_len = send_trades(trade_list)
logger.info('Number of Trades: {}'.format(trade_len))






