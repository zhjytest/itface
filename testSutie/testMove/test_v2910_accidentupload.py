#coding:utf-8

from config import *
from frameUtil.get_info import get_loadresult,generate_randstr
from frameUtil.rwfile import get_pwd
from random import  choice,randint

class Test_accidentupload():
    '''事故上报'''

    def setup_class(self):
        self.orderid =  71649
        self.url = get_urls("/accident/upload.html",3)
        key = get_key()
        uid = get_id()
        self.parm = get_parm()
        self.parm['uid'] = uid
        self.parm['key'] = key
        self.parm['order_id'] = self.orderid
        self.parm['city_id'] = 1


    def test_a_upload(self):
        self.parm['action'] = 'upload'
        self.parm['type'] = 2
        self.parm['content'] = 'test'
        result = get_loadresult(self.url,self.parm)
        print(result)
        assert result['status'] == 0
        assert result['msg'] == '提交成功'


    def test_b_info(self):
        self.parm['action'] = 'c_info'
        result = get_loadresult(self.url,self.parm)
        print(result)
        assert result['status'] == 0

    def test_c_list(self):
        self.parm['action'] = 'list'
        result = get_loadresult(self.url,self.parm)
        print(result)
        assert result['data'][0]['order_id'] == str(self.orderid)


