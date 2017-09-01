#coding:utf-8

from config import *
from frameUtil.get_info import get_loadresult,generate_randstr,get_fileresult
from random import  choice,randint
from db.sqlconn import Mysql
from time import sleep
import pytest

class Test_breakdetail():


    def setup_class(self):
        #新的接口地址
        self.url_new = get_urls("/api/get_rec_car.php",5)
        key = get_key()
        self.uid = get_id()
        parm_new = get_parm()
        parm_new['uid'] = self.uid
        parm_new['key'] = key
        parm_new['ret_wd_id'] = 475
        parm_new['wd_id'] = 786
        parm_new['city'] = '广州市'
        parm_new['city_id'] = 197
        self.parm_new = parm_new
        print(self.parm_new)
        self.result_new = get_loadresult(self.url_new,self.parm_new)
        print(self.result_new)
        print("动态价格：",self.result_new['data'][0]['dyn_price'])
        print("里程：",self.result_new['data'][0]['discount_value'])




    def test_commit(self):
        assert  1 == 2







