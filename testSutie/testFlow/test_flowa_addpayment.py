#coding:utf-8
from config import *
from frameUtil.get_info import get_loadresult
import pytest
from random import choice,randint
#from config import get_id,get_mobile


class Test_selfservicepayment:
    """
        功能：创建自助缴费单(非保险)
    """

    def setup_class(self):
        #1.创建自助缴费单(非保险类) ，返回pkid
        self.add_url = get_urls("/v1/workorder/jiaofei/add",1)
        self.parm1 = {}
        self.mobile = get_mobile()   #获取用户手机号
        self.uid =  int(get_id())        #获取用户uid
        print("获取到的手机号:",self.mobile)
        print("获取用户uid：",self.uid)
        types = [1,2,3,4,5,6,8]
        self.tyvalue = choice(types)
        #=====================
        self.money = randint(1,10000)
        print("money:",self.money)
        print("tyvalue:",self.tyvalue)
        self.parm1['mobile'] = self.mobile
        self.parm1['types'] = self.tyvalue
        self.parm1['money'] = self.money
        self.parm1['tour_id'] = 69567          #行程id写死了
        self.parm1['create_uid'] = self.uid
        self.parm1['create_flatform'] = 1
        print("当前参数列表：",self.parm1)
        self.result = get_loadresult(self.add_url,self.parm1)
        print("返回的结果:",self.result)
        status = self.result['status']
        if status == 0:
            pkid = self.result['data']['pkid']
            print("pkid:",pkid)
            set_pkid(pkid)
            set_money(self.money)
            set_type(self.tyvalue)
        else:
            set_pkid(568)
            set_money(406)
            set_type(5)

        #2.通过


    def test_flow_payment(self):
        assert self.result['msg'] == '请求成功'

