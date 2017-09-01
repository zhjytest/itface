#coding:utf-8

from config import *
from frameUtil.get_info import get_loadresult
from random import  choice,randint
#from db.data_manage import data_manage

class Test_create_invoic():


    def setup_class(self):
        #新的接口地址
        self.url_new = get_urls("/invoice/create.html",3)
        self.uid = get_id()
        key = get_key()
        type = self.status = choice(['1','2'])
        money = randint(200,800)
        parm_new = get_parm()
        parm_new['uid'] = self.uid
        parm_new['type'] = type
        parm_new['title'] = 'testtitle'
        parm_new['content'] = 'testxxx'
        parm_new['money'] = money
        parm_new['name'] = '测试者'
        parm_new['address'] = '酒仙桥路'
        parm_new['city'] = '北京市'
        parm_new['mobile'] = get_mobile()
        parm_new['tax_no'] = '123456789123456789'
        self.parm_new = parm_new
        #self.result_new = get_loadresult(self.url_new,self.parm_new)
        #print("开发票（新）:",self.result_new)
        #老的接口地址
        self.url_old = get_urls("/api/invoice.php",5)
        parm_old = get_parm()
        parm_old['uid'] = self.uid
        parm_old['key'] = key
        parm_old['type'] = type
        parm_old['title'] = 'testtitle'
        parm_old['content'] = 'testxxx'
        parm_old['money'] = money
        parm_old['name'] = '测试者'
        parm_old['address'] = '酒仙桥路'
        parm_old['city'] = '北京市'
        parm_old['mobile'] = get_mobile()
        parm_old['tax_no'] = '123456789123456789'
        self.parm_old = parm_old
        #self.result_old = get_loadresult(url_old,parm_old)
        #print("开发票（老）:",self.result_old)


    def test_compare_result(self):
        self.result_new = get_loadresult(self.url_new,self.parm_new)
        print("开发票（新）:",self.result_new)
        self.result_old = get_loadresult(self.url_old,self.parm_old)
        print("开发票（老）:",self.result_old)
        assert self.result_new['status'] == self.result_old['status']

    # def test_status_change(self):
    #     print("uid:::",self.uid,"==status:::",self.status)
    #     dp = data_manage()
    #     dp.update_invoic(self.uid,self.status)
    #     #dp.select_test(self.uid)

