
import urllib.request
import json
import db
import re
import time
from bs4 import BeautifulSoup


def stock_api_url():
    url = 'http://apis.baidu.com/tehir/stockassistant/stocklist'
    header = {"apikey": "a8b745966efa4e9159cf9ec2b83d2133"}
    req = urllib.request.Request(url=url, headers=header)
    data = urllib.request.urlopen(req).read().decode('utf-8')
    return json.loads(data)


def xueqiu_url(url):
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'}
    req = urllib.request.Request(url=url, headers=header)
    return urllib.request.urlopen(req).read().decode('utf-8')


def add_stock_base_info(stock_list):
        i = 0
        for rows in stock_list['rows']:
            db.add_stock_base_info(rows)
            i = i + 1
            print(i)

            # print('%s=' % i,rows[i])
        print('-------------------------------')


def loop_xueqiu():
    urlSH= 'https://xueqiu.com/S/SH%s/follows'
    urlSZ= 'https://xueqiu.com/S/SZ%s/follows'
    stocklist = db.get_stock_list()
    for stock in stocklist:
        code = stock[0]
        if code[0] == '6':
            url = urlSH % code
        else:
            url = urlSZ % code
        html = xueqiu_url(url)
        soup = BeautifulSoup(html, 'lxml')
        str2 = soup.find('div', {'class': 'stockInfo'}).contents
        b = re.search(r"\((.*?)\)", str(str2[1])).groups()
        # str2 = soup.select('span')
        # b = re.search(r"\((.*?)\)", str(str2[1])).groups()

        print(b[0], code)


loop_xueqiu()










