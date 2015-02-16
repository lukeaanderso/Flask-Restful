__author__ = 'landerson'

from flask import Flask
from flask.ext import restful

from server import DataApi, TradeApi


app = Flask(__name__)
api = restful.Api(app)

api.add_resource(DataApi, '/data/')
api.add_resource(TradeApi, '/trade/')