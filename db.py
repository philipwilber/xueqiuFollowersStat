import sqlite3


def createdb():

    conn = sqlite3.connect('stock_base.db')
    cursor = conn.cursor()
    sql = '''create table stock_base (code varchar(20) primary key,
                                     name nvarchar(10),
                                     industry nvarchar(20),
                                     area nvarchar(10),
                                     pe float,
                                     outstanding float,
                                     totals float,
                                     totalassets float,
                                     liquidassets float,
                                     fixedassets float,
                                     reserved float,
                                     reservedpershare float,
                                     eps float,
                                     bvps float,
                                     pb float,
                                     timetomarket date
                                      )'''
    cursor.execute(sql)
    cursor.close()
    conn.commit()
    conn.close()


def add_stock_base_info(data):

    conn = sqlite3.connect('stock_base.db')
    cursor = conn.cursor()
    sql = '''insert into stock_base (code,name,industry,area,pe,outstanding,totals,totalassets,
             liquidassets,fixedassets,reserved,reservedpershare,eps,bvps,pb,timetomarket)
             values ('%s','%s','%s','%s',%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,%f,'%s')
             ''' % (data['code'], data['name'], data['industry'], data['area'], data['pe'], data['outstanding'],
                    data['totals'], data['totalassets'],data['liquidassets'],data['fixedassets'],
                    data['reserved'],data['reservedpershare'],data['eps'],data['bvps'],data['pb'],data['timetomarket'])
    cursor.execute(sql)
    cursor.close()
    conn.commit()
    conn.close()


def get_stock_list():
    conn = sqlite3.connect('stock_base.db')
    cursor = conn.cursor()
    sql = 'select code, name from stock_base'
    cursor.execute(sql)
    value = cursor.fetchall()
    cursor.close()
    conn.close()
    return value
