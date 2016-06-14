
import urllib.request
import json
import re
import time
from bs4 import BeautifulSoup
from db import DBProvider

dbProvider = DBProvider()

def stock_api_url():
    url = 'http://apis.baidu.com/tehir/stockassistant/stocklist'
    header = {"apikey": "a8b745966efa4e9159cf9ec2b83d2133"}
    req = urllib.request.Request(url=url, headers=header)
    data = urllib.request.urlopen(req).read().decode('utf-8')
    return json.loads(data)


def get_url(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'}
    req = urllib.request.Request(url=url, headers=header)
    return urllib.request.urlopen(req).read()


def cre_stock_base_db(stock_list):
        i = 0
        for rows in stock_list['rows']:
            dbProvider.add_stock_base_info(rows)
            code = rows['code']
            dbProvider.createIndividStockDB(code)
            i = i + 1
            print(i, code)

            # print('%s=' % i,rows[i])
        print('-------------------------------')


def loop_xueqiu():
    url1= 'https://xueqiu.com/S/%s/follows'
    url2 = 'http://qt.gtimg.cn/q='
    stocklist = db.get_stock_list()
    for stock in stocklist:
        code = stock[0]
        if code[0] == '6':
            code_full = 'SH' + code
        else:
            code_full = 'SZ' + code

        url_follows = url1 % code_full
        html_follows = get_url(url_follows)
        soup_follows = BeautifulSoup(html_follows, 'lxml')
        str_follows = soup_follows.find('div', {'class': 'stockInfo'}).contents
        follows = re.search(r"\((.*?)\)", str(str_follows[1])).groups()

        url_info = url2 + code_full
        html_info = str(get_url(url_info.lower()))
        stockDetail = {}
        stockInfo = html_info.split('~')


        # stock daily info
        # data_follows = xueqiu_url(url_info+code_full)
        print(follows[0])
        print(type(html_info))
        # print(b[0], code)

def creDB():
    stocklist = db.get_stock_list()
    for stock in stocklist:
        code = stock[0]
        if code[0] == '6':
            code_full = 'SH' + code
        else:
            code_full = 'SZ' + code

if __name__ == '__main__':
    dbProvider.dbConn()
    cre_stock_base_db(stock_api_url())
    dbProvider.dbClose()



