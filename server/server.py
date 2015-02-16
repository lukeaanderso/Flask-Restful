__author__ = 'landerson'
import pickle as pickle

from flask import request
from flask.ext import restful

from api._logging import setup

from api.pricing import get_yahoo

logger = setup('Rest API')


def convert_tradelist(obj):
    tradelist = pickle.loads(obj)
    return tradelist


def process_trades(trade_list=None):
    for trd in trade_list:
        logger.info('Processing Trade: {}'.format(trd))
        # Prove that we have the full classes
        logger.info('Sending to {} at {}'.format(trd.broker.desk, trd.broker.broker_name))
    return len(trade_list)


def get_data(symbol=None, date=None, field=None):
    msg = 'Request Recieved. Symbol: {} Date: {} Field: {}'
    msg = msg.format(symbol, date, field)
    logger.info(msg)
    data = get_yahoo(symbol, date, field)
    return data


class DataApi(restful.Resource):
    def put(self):
        data = request.form.to_dict()
        res = get_data(**data)
        return {'result': res}


class TradeApi(restful.Resource):
    def put(self):
        data = request.form.to_dict()
        tradelist = convert_tradelist(data['trade_list'])
        res = process_trades(tradelist)
        return res