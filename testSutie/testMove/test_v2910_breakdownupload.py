#coding:utf-8

from config import *
from frameUtil.get_info import get_loadresult,generate_randstr,get_fileresult
from frameUtil.rwfile import get_pwd
from random import  choice,randint
from db.sqlconn import Mysql
from time import sleep
import pytest

class Test_breakdownupload():
    '''故障详情'''

    def setup_class(self):
        #新的接口地址
        self.url = get_urls("/break-down/upload.html",3)
        self.uid = get_id()
        sql = "select id from 630_tour where customer_id = '%s' ORDER BY id DESC" % (self.uid)
        self.db = Mysql()
        self.ddid = self.db.getRandomOne(sql)
        key = get_key()
        self.content = generate_randstr()
        self.parm = get_parm()
        ##self.ddid = dm.select_tourddid(self.uid)
        print("ddid::::::",self.ddid)
        self.parm['uid'] = self.uid
        self.parm['key'] = key
        self.parm['order_id'] = self.ddid



    def test_a_upload(self):
        x = randint(1,8)
        self.parm['break_units'] = x
        self.parm['action'] = 'upload'
        self.parm['content'] = self.content
        fpwd = get_pwd('test.jpg')
        print(fpwd)
        files = {'file':open(fpwd,'rb')}
        #files = {'file':open('d:/project/pyinterface/yditface/tools/test.jpg','rb')}
        result = ''
        if x == 8:
            result = get_fileresult(self.url,self.parm,files)
        else:
            result = get_loadresult(self.url,self.parm)
        print("故障反馈提交后:",result)
        assert result['status']  == 0

    def test_b_list(self):
        self.parm['action'] = 'list'
        result = get_loadresult(self.url,self.parm)
        print(result)
        assert result['status']  == 0
        if result['data'][0]['pics']:
            assert 'https://imgtest.yiduyongche.com/feedback/feedback' in result['data'][0]['pics'][0]
        assert result['data'][0]['order_id'] == str(self.ddid)
        assert result['data'][0]['content'] == self.content




    def teardown_class(self):
        self.db.dispose()









