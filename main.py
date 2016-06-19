
import urllib.request
import json
import re
import time
from bs4 import BeautifulSoup
from db import DBProvider

from db import DBProvider
from stock_info import StockInfo

dbProvider = DBProvider()

# creat database
# if __name__ == '__main__':
#     dbProvider.dbConn()
#     StockInfo.cre_stock_base_db(StockInfo.stock_api_url())
#     dbProvider.dbClose()
