import json
import re
import urllib.request

from bs4 import BeautifulSoup

from app_const.app_consts import Const
from db import DBProvider

dbProvider = DBProvider(object)


class StockInfo:

    def stock_api_url(self):
        url = Const.MAIL_PROTO_IMAP
        header = Const.STOCK_API_HEADER
        req = urllib.request.Request(url=url, headers=header)
        data = urllib.request.urlopen(req).read().decode('utf-8')
        return json.loads(data)

    def get_url(self, url):
        header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'}
        req = urllib.request.Request(url=url, headers=header)
        return urllib.request.urlopen(req).read()

    def cre_stock_base_db(self, stock_list):
        i = 0
        for rows in stock_list['rows']:
            dbProvider.add_stock_base_info(rows)
            code = rows['code']
            dbProvider.createIndividStockDB("'" + code + "'")
            i = i + 1
            print(i, code)

            # print('%s=' % i,rows[i])
        print('-------------------------------')

    def add_xueqiu_daily(self):
        url1 = Const.XUEQIU_URL_1

        stocklist = dbProvider.get_stock_list()
        for stock in stocklist:
            code = stock[0]
            if code[0] == '6':
                code_full = 'SH' + code
            else:
                code_full = 'SZ' + code

            url_follows = url1 % code_full
            html_follows = self.get_url(url_follows)
            soup_follows = BeautifulSoup(html_follows, 'lxml')
            str_follows = soup_follows.find('div', {'class': 'stockInfo'}).contents
            follows = re.search(r"\((.*?)\)", str(str_follows[1])).groups()



            # stock daily info
            # data_follows = xueqiu_url(url_info+code_full)
            print(follows[0])
            # print(b[0], code)

    def get_stock_daily(self, code_full):
        url = Const.TENCENT_STOCK_URL_1
        url_info = url + code_full
        html_info = str(self.get_url(url_info.lower()))
        stockDetail = {}
        stockInfo = html_info.split('~')
            # creat database
            # if __name__ == '__main__':
            #     dbProvider.dbConn()
            #     cre_stock_base_db(stock_api_url())
            #     dbProvider.dbClose()





