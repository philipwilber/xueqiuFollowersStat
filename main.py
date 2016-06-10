
import urllib.request
import json
import db
import re
import time
from bs4 import BeautifulSoup


url= 'http://apis.baidu.com/tehir/stockassistant/stocklist'
header = {"apikey": "a8b745966efa4e9159cf9ec2b83d2133"}
req = urllib.request.Request(url=url, headers=header)
data = urllib.request.urlopen(req).read().decode('utf-8')
decode = json.loads(data)

def add_stock_base_info(stock_list):
        i = 0
        for rows in stock_list['rows']:
            db.add_stock_base_info(rows)
            i = i + 1
            print(i)

            # print('%s=' % i,rows[i])
        print('-------------------------------')


def loop_xueqiu(stock_list):
    urlSH= 'https://xueqiu.com/S/SH'
    urlSZ= 'https://xueqiu.com/S/SZ'
    for rows in stock_list['rows']:
        code = rows['code']


