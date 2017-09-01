#coding:utf-8

from config import *
from frameUtil.get_info import get_loadresult,generate_randstr
from frameUtil.rwfile import get_pwd
from random import  choice,randint

class Test_choosecar():
    '''当前行程信息'''

    def setup_class(self):
        self.url = get_urls("/choose-car/index.html",3)
        key = get_key()
        uid = get_id()
        self.parm = get_parm()
        self.parm['uid'] = uid
        self.parm['key'] = key
        self.parm['wd_id'] = '416'
        self.parm['ret_wd_id'] = '416'
        #par['car_id'] = ''
        #定义变量
        #self.chekuan = ['华泰','北汽','江淮','吉利','康迪','江铃','奇瑞','现代','众泰','比亚迪']


    #用例1：手动选择用车
    def test_choose(self):
        result = get_loadresult(self.url,self.parm)
        print(result)
        assert result['status'] == 0
        assert result['data'][0]['chepai'] != None
        assert result['data'][0]['dyn_price'] in [0,3,5]
        assert result['data'][0]['price_min'] == '0.15'
        assert result['data'][0]['price_km'] == '1.50'

    #用例2：扫码用车#
    def test_scan(self):
        self.parm['car_id'] = '187'
        result = get_loadresult(self.url,self.parm)
        print(result)
        assert result['status'] == 0
        assert result['data'][0]['dyn_price'] in [0,3,5]
        assert result['data'][0]['price_min'] == '0.15'
        assert result['data'][0]['price_km'] == '1.50'