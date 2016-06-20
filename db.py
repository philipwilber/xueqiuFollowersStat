import sqlite3


class DBProvider(object):

    def dbConn(self):
        self.conn = sqlite3.connect('IDB_MAIN.db')
        return self.conn

    def dbClose(self):
        if(self.conn != None):
            self.conn.close()

    def execute(self, sql):
        try:
            if(self.conn != None):
                cursor = self.conn.cursor()
            else:
                raise sqlite3.Error('Connection Error')

            n = cursor.execute(sql)
            return n
        except sqlite3.Error:
            print('')

    def createStockDB(self):
        try:
            if(self.conn != None):
                cursor = self.conn.cursor()
            else:
                raise sqlite3.Error('Connection Error')

            sql = '''create table stock_base (code varchar(9) primary key,
                                     name nvarchar(10),
                                     industry nvarchar(10),
                                     area nvarchar(10),
                                     pe DECIMAL(15,3),
                                     outstanding DECIMAL(15,3),
                                     totals DECIMAL(15,3),
                                     totalassets DECIMAL(15,3),
                                     liquidassets DECIMAL(15,3),
                                     fixedassets DECIMAL(15,3),
                                     reserved DECIMAL(15,3),
                                     reservedpershare DECIMAL(10,5),
                                     eps DECIMAL(10,5),
                                     bvps DECIMAL(10,5),
                                     pb DECIMAL(10,5),
                                     timetomarket date
                                      )
                                      '''
            cursor.execute(sql)
            self.conn.commit()
            cursor.close()
        except sqlite3.Error:
            self.conn.rollback()

    def createIndividStockDB(self, stockCode):
        try:
            if(self.conn != None):
                cursor = self.conn.cursor()
            else:
                raise sqlite3.Error('Connection Error')

            sql = '''create table %s (id INTEGER PRIMARY KEY,
                                     cre_dt date UNIQUE,
                                     follows INTEGER,
                                     price DECIMAL(7,3),
                                     yesterday_close DECIMAL(7,3),
                                     today_open DECIMAL(7,3),
                                     volume INTEGER,
                                     outer_sell INTEGER,
                                     inner_buy INTEGER,
                                     buy_one DECIMAL(7,3),
                                     buy_one_volume INTEGER,
                                     buy_two DECIMAL(7,3),
                                     buy_two_volume INTEGER,
                                     buy_three DECIMAL(7,3),
                                     buy_three_volume INTEGER,
                                     buy_four DECIMAL(7,3),
                                     buy_four_volume INTEGER,
                                     buy_five DECIMAL(7,3),
                                     buy_five_volume INTEGER,
                                     sell_one DECIMAL(7,3),
                                     sell_one_volume INTEGER,
                                     sell_two DECIMAL(7,3),
                                     sell_two_volume INTEGER,
                                     sell_three DECIMAL(7,3),
                                     sell_three_volume INTEGER,
                                     sell_four DECIMAL(7,3),
                                     sell_four_volume INTEGER,
                                     sell_five DECIMAL(7,3),
                                     sell_five_volume INTEGER,
                                     date_time DATETIME,
                                     updown FLOAT,
                                     updown_rate FLOAT,
                                     heighest_price DECIMAL(7,3),
                                     lowest_price DECIMAL(7,3),
                                     volume_amout INTEGER,
                                     turnover_rate FLOAT,
                                     pe_rate FLOAT,
                                     viberation_rate FLOAT,
                                     circulated_stock DECIMAL(15,3),
                                     total_stock DECIMAL(15,3),
                                     pb_rate FLOAT,
                                     update_dt DATE
                                      )
                                      ''' % stockCode
            cursor.execute(sql)
            self.conn.commit()
            cursor.close()
        except sqlite3.Error:
            self.conn.rollback()

    def add_stock_base_info(self, data):
        try:
            if(self.conn != None):
                cursor = self.conn.cursor()
            else:
                raise sqlite3.Error('Connection Error')

            sql = '''insert into stock_base (code,name,industry,area,pe,outstanding,totals,totalassets,
             liquidassets,fixedassets,reserved,reservedpershare,eps,bvps,pb,timetomarket)
             values ('%s','%s','%s','%s',%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,'%s')
             ''' % (data['code'], data['name'], data['industry'], data['area'], data['pe'], data['outstanding'],
                    data['totals'], data['totalassets'], data['liquidassets'], data['fixedassets'],
                    data['reserved'], data['reservedpershare'], data['eps'], data['bvps'], data['pb'], data['timetomarket'])

            cursor.execute(sql)
            self.conn.commit()
            cursor.close()
        except sqlite3.Error:
            self.conn.rollback()

    def get_stock_list(self, db):
        try:
            if (self.conn != None):
                cursor = self.conn.cursor()
            else:
                raise sqlite3.Error('Connection Error')

                sql = 'select code, name from stock_base'
            cursor.execute(sql)
            self.conn.commit()
            value = cursor.fetchall()
            cursor.close()
            return value
        except sqlite3.Error:
            self.conn.rollback()

    def add_stock_daliy(self, follows, data):
        try:
            if (self.conn != None):
                cursor = self.conn.cursor()
            else:
                raise sqlite3.Error('Connection Error')

            sql = '''insert into ''' + data[0] + ''' (cre_dt,follows,price,yesterday_close,today_open,volume,outer_sell,
                     inner_buy,buy_one,buy_one_volume,buy_two,buy_two_volume,buy_three,buy_three_volume,buy_four,
                     buy_four_volume,buy_five,buy_five_volume,sell_one,sell_one_volume,sell_two,sell_two_volume,
                     sell_three,sell_three_volume,sell_four,sell_four_volume,sell_five,sell_five_volume,date_time,
                     updown,updown_rate,heighest_price,lowest_price,volume_amout,turnover_rate,pe_rate,viberation_rate,
                     circulated_stock,total_stock,pb_rate)
                     values (date('now'),'%s','%s','%s','%s','%s',%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,'%s')
                     ''' % (follows, data[0], data[1], )

            cursor.execute(sql)
            self.conn.commit()
            cursor.close()
        except sqlite3.Error:
            self.conn.rollback()

    def is_stock_daily_data_existed(self, table, date):
        try:
            if(self.conn != None):
                cursor = self.conn.cursor()
            else:
                raise sqlite3.Error('Connection Error')

            sql = "select id from %s where cre_dt = '%s'" % (table, date)
            n = cursor.execute(sql)
            if n >= 1:
                return True
        except sqlite3.Error:
            print('')
