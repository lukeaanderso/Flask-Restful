__author__ = 'landerson'

from collections import namedtuple

trade = namedtuple('trade', ['account', 'symbol', 'shares', 'px', 'broker'])
broker = namedtuple('broker', ['broker_id', 'broker_name', 'desk'])

brokerlist = namedtuple('brokerlist', ['ms'])

brokers = brokerlist(ms=broker(1, 'Morgan Stanley', 'US Equities'))
