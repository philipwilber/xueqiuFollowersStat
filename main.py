
import urllib.request
import json
import re
import datetime
from bs4 import BeautifulSoup
from db import DBProvider

from db import DBProvider
from stock_info import StockInfo


# creat database
# if __name__ == '__main__':
#     stock = StockInfo()
#     stock.db_conn()
#     stock.cre_stock_base_db(stock.stock_api_url())
#     stock.db_close()

#insert daily data
if __name__ == '__main__':
     stock = StockInfo()
     # date = datetime.datetime.now().strftime("%Y-%m-%d")
     date = '2016-07-20'
     stock.add_daily_data(date)
     # stock.get_stock_daily('SZ300368')

