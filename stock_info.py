import json
import re
import urllib.request
from bs4 import BeautifulSoup

import threading
import time

from consts import const
from db import DBProvider

dbProvider = DBProvider()
class StockInfo:

    def db_conn(self):
        return dbProvider.dbConn()

    def db_close(self):
        return dbProvider.dbClose()

    def stock_api_url(self):
        url = const.STOCK_API
        header = const.STOCK_API_HEADER
        req = urllib.request.Request(url=url, headers=header)
        data = urllib.request.urlopen(req).read().decode('utf-8')
        return json.loads(data)

    def get_url(self, url):
        header = const.URL_HEADER
        req = urllib.request.Request(url=url, headers=header)
        return urllib.request.urlopen(req).read()

    def cre_stock_base_db(self, stock_list):
        dbProvider.createStockDB()
        print('stock')
        i = 0
        for rows in stock_list['rows']:
            dbProvider.add_stock_base_info(rows)
            code = rows['code']
            dbProvider.createIndividStockDB("'" + code + "'")
            i = i + 1
            print(i, code)

            # print('%s=' % i,rows[i])
        print('-------------------------------')
        dbProvider.dbClose()

    def get_stock_list(self):
        return dbProvider.get_stock_list()

    def get_xueqiu_follows_daily(self, code):
        url1 = const.XUEQIU_URL_1
        # if code == '6':
        #     code = 'SH' + code
        # else:
        #     code = 'SZ' + code

        url1 = url1 % code
        # time.sleep(1)
        html_follows = self.get_url(url1)
        soup_follows = BeautifulSoup(html_follows, 'lxml')
        str_follows = soup_follows.find(
            'div', {'class': 'stockInfo'}).contents
        follows = re.search(r"\((.*?)\)", str(str_follows[1])).groups()
        return follows[0]

        # print(follows[0])
        # print(b[0], code)

    def __is_stock_daily_data_exited(self, table, date):
        self.db_conn()
        value = dbProvider.is_stock_daily_data_existed(table, date)
        self.db_close()
        return value

    def get_stock_daily(self, code_full):
        url = const.TENCENT_STOCK_URL_1
        url = url + code_full
        tempData = str(self.get_url(url.lower()))

        if tempData == None:
            time.sleep(10)
            tempData = str(self.get_url(url.lower()))
            return False

        stock_data = {}
        stockInfo = tempData.split('~')
        if len(stockInfo) < 45:
            return
        if len(stockInfo) != 0 and stockInfo[0].find('pv_none') == -1 and stockInfo[3].find('0.00') == -1:
            table = stockInfo[2]
            date = stockInfo[30]
            if not self.__is_stock_daily_data_exited(table, date):
                stock_data['code'] = stockInfo[2]
                stock_data['price'] = stockInfo[3]
                stock_data['yesterday_close'] = stockInfo[4]
                stock_data['today_open'] = stockInfo[5]
                stock_data['volume'] = stockInfo[6]
                stock_data['outer_sell'] = stockInfo[7]
                stock_data['inner_buy'] = stockInfo[8]
                stock_data['buy_one'] = stockInfo[9]
                stock_data['buy_one_volume'] = stockInfo[10]
                stock_data['buy_two'] = stockInfo[11]
                stock_data['buy_two_volume'] = stockInfo[12]
                stock_data['buy_three'] = stockInfo[13]
                stock_data['buy_three_volume'] = stockInfo[14]
                stock_data['buy_four'] = stockInfo[15]
                stock_data['buy_four_volume'] = stockInfo[16]
                stock_data['buy_five'] = stockInfo[17]
                stock_data['buy_five_volume'] = stockInfo[18]
                stock_data['sell_one'] = stockInfo[19]
                stock_data['sell_one_volume'] = stockInfo[20]
                stock_data['sell_two'] = stockInfo[22]
                stock_data['sell_two_volume'] = stockInfo[22]
                stock_data['sell_three'] = stockInfo[23]
                stock_data['sell_three_volume'] = stockInfo[24]
                stock_data['sell_four'] = stockInfo[25]
                stock_data['sell_four_volume'] = stockInfo[26]
                stock_data['sell_five'] = stockInfo[27]
                stock_data['sell_five_volume'] = stockInfo[28]
                stock_data['datetime'] = stockInfo[30]
                stock_data['updown'] = stockInfo[31]
                stock_data['updown_rate'] = stockInfo[32]
                stock_data['heighest_price'] = stockInfo[33]
                stock_data['lowest_price'] = stockInfo[34]
                stock_data['volume_amout'] = stockInfo[35].split('/')[2]
                stock_data['turnover_rate'] = stockInfo[38]
                stock_data['pe_rate'] = stockInfo[39]
                stock_data['viberation_rate'] = stockInfo[42]
                stock_data['circulated_stock'] = stockInfo[43]
                stock_data['total_stock'] = stockInfo[44]
                stock_data['pb_rate'] = stockInfo[45]
                return stock_data

    def add_daily_data(self, date):

        stocklist = self.get_stock_list()
        for stock in stocklist:
            self.db_conn()
            code = stock[0]
            if code[0] == '6':
                code_full = 'SH' + code
            else:
                code_full = 'SZ' + code
            follows = self.get_xueqiu_follows_daily(code_full)
            stock_data = self.get_stock_daily(code_full)
            if(follows != None and stock_data != None):
                value = dbProvider.add_stock_daliy(date, follows, stock_data)
                print('%s 加入数据成功 %s' % (code_full, value))
            else:
                print('%s 加入数据失败' % code_full)
            self.db_close()



