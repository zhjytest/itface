#coding:utf-8

from config import get_parm,get_urls,get_id,get_key,set_bx_money
from frameUtil.get_info import get_loadresult
from random import choice,randint
from time import sleep

class Test_createaccident:
    """
        version:2.9.3
        author:zhangjiangyu
        time:2017.07.04
        功能:创建事故单  ---管理APP，为了创建保险费而创建的工单
    """
    accid = 0

    def get_num(self):
        num = randint(1,5000)
        num = float(num)
        return num

    def setup_class(self):
        #创建事故单
        lst = [0,1]
        lst1 = [0,1,2]   #责任方
        self.url = get_urls("/index.php?r=accident/create",2)
        parm = get_parm()
        uid = get_id()
        key = get_key()
        parm['car_id'] = 690
        parm['accident_type'] = choice(lst)
        parm["people_hurt"] = choice(lst)
        parm["blamed_type"] = choice(lst1)
        parm["tour_id"] = 69292
        parm["customer_id"] = uid
        parm["create_uid"] = 225
        parm["content"] = 'test'
        parm["happen_time"] = 2017-7-4
        self.parm = parm
        self.result = get_loadresult(self.url,self.parm)
        print("创建保险单返回的数据，create_accident：",self.result)
        #print(self.result)
        #返回结果：{"status":0,"msg":"","data":{"accidentId":"3"}}
        self.accid = self.result['data']['accidentId']
        print("accid:",self.accid)
        #return self.accid



    def selectsave(self):
        #走保险流程
        print("这里渠道的accid：",self.accid)
        self.url = get_urls("/index.php?r=accident/selectsave",2)
        parm = get_parm()
        #uid = get_id()
        key = get_key()
        parm["accident_id"] = self.accid
        parm["is_save"] = 1  #1代表走保险流程
        self.parm = parm
        self.result = get_loadresult(self.url,self.parm)
        #返回的结果：{"status":0,"msg":"修改成功","data":[]}
        print("走保险流程返回的数据，selectsave：",self.result)
        status = self.result['status']
        return status


    def addpayment(self):
        #客户预交保险添加
        self.url = get_urls("/index.php?r=accident/addpayment",2)
        parm = get_parm()
        #uid = get_id()
        key = get_key()
        parm["uid"] = 225
        parm["accident_id"] = self.accid
        parm["money"] = self.get_num()  #客户缴的费用
        self.parm = parm
        self.result = get_loadresult(self.url,self.parm)
        print("预交保险费返回的数据，addpayment：",self.result)
        #返回的结果：{"status":0,"msg":"修改成功","data":[]}
        status = self.result['status']
        set_bx_money(self.get_num())
        return status

    def test_selectsave(self):
        assert self.selectsave() == 1

    def test_status(self):
        sleep(0.5)
        assert self.addpayment() == 0


