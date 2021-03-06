#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
PROJECT_NAME:TradingBot
NAME:Dao
AUTHOR:Tong
Create Date:2018/4/14
'''
from Dao import *
from Dao.MysqlUtil import Mysql
import time
import json

class diff_btcusdt_binance_huobi_dao():
    def __init__(self):
        database = json.loads(open("../database.json", "r").read())
        self.table_name = 'diff_btcusdt_binance_huobi'
        self.mysql = Mysql(host=database['host'], user=database['user'], password=database['password'], database=database['database'], port=database['port'])

    def insert(self, po):
        insert_sql = '''INSERT INTO diff_btcusdt_binance_huobi VALUES (null, %s,%s,%s,%s,%s,%s)'''
        value = (getattr(po, 'symbol'), getattr(po, 'ask_price1'), getattr(po, 'bid_price1'), getattr(po, 'ask_price2'), getattr(po, 'bid_price2'), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

        self.mysql.insert(insert_sql, value)

    def delete(self, po):
        pass

    def update(self, po):
        pass

    def query(self, po):
        pass

class porting_flow_dao:
    def __init__(self):
        database = json.loads(open("../database.json", "r").read())
        self.table_name = 'porting_flow'
        self.mysql = Mysql(host=database['host'], user=database['user'], password=database['password'], database=database['database'], port=database['port'])

    def insert(self, po):
        insert_sql = '''INSERT INTO porting_flow VALUES (null, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        value = (getattr(po, 'symbol'), getattr(po, 'tradingIdMarket1'), getattr(po, 'tradingIdMarket2'), getattr(po, 'isMarket1Success'), getattr(po, 'isMarket2Success'), getattr(po, 'amountMarket1'), getattr(po, 'amountMarket2'), getattr(po, 'priceMarket1'), getattr(po, 'priceMarket2'), time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

        self.mysql.insert(insert_sql, value)

    def delete(self, po):
        pass

    def update(self, po):
        pass

    def query(self, po):
        pass
