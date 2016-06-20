class _const:
    class ConstError( TypeError ): pass
    class ConstCaseError( ConstError ): pass

    def __setattr__( self, name, value ):
        if name in self.__dict__:
            raise self.ConstError( "can't change const %s" % name )
        if not name.isupper():
            raise self.ConstCaseError( 'const name "%s" is not all uppercase' % name )
        self.__dict__[name] = value

const = _const()
const.STOCK_API = 'http://apis.baidu.com/tehir/stockassistant/stocklist'
const.STOCK_API_HEADER = {"apikey": "a8b745966efa4e9159cf9ec2b83d2133"}
const.XUEQIU_URL_1 = 'https://xueqiu.com/S/%s/follows'
const.TENCENT_STOCK_URL_1 = 'http://qt.gtimg.cn/q='
const.URL_HEADER = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'}