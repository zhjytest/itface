#coding:utf-8

from config import *
from frameUtil.get_info import get_loadresult,generate_randstr
from frameUtil.rwfile import get_pwd
from random import  choice,randint
from db.sqlconn import Mysql

class Test_codeuse():
    '''兑换优惠券'''

    def setup_class(self):
        url = get_urls("/code/use.html",3)
        sql = "SELECT code from 630_customer WHERE code != ''"
        self.db = Mysql()
        code = self.db.getRandomOne(sql)
        print("code:",code)
        key = get_key()
        uid = get_id()
        parm = get_parm()
        parm['uid'] = uid
        parm['key'] = key
        parm['code'] = code
        self.result = get_loadresult(url,parm)
        print(self.result)


    def test_data(self):
        status = self.result['status']
        if status == 0:
            assert self.result['msg'] == '使用推荐码成功!'
        else:
            assert self.result['msg'] == '您使用过其他人的推荐码!'
        #assert 1 == 2


    def teardown_class(self):
        self.db.dispose()

