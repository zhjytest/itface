#coding:utf-8

from config import *
from frameUtil.get_info import get_loadresult


class Test_invoicerecode():


    def setup_class(self):
        #新的接口地址
        self.url_new = get_urls("/invoice/record.html",3)
        uid = get_id()
        key = get_key()
        parm_new = get_parm()
        parm_new['uid'] = uid
        self.parm_new = parm_new
        self.result_new = get_loadresult(self.url_new,self.parm_new)
        print("发票记录列表（新）:",self.result_new)
        #老的接口地址
        url_old = get_urls("/api/get_user_info.php",5)
        parm_old = get_parm()
        parm_old['uid'] = uid
        parm_old['key'] = key
        parm_old['type'] = 'invoice'
        self.result_old = get_loadresult(url_old,parm_old)
        print("发票记录列表（老）:",self.result_old)



    def test_compare_result(self):
        assert self.result_old['status'] == self.result_new['status'] == 0
        assert len(self.result_old['data']) == len(self.result_new['data'])
        assert self.result_old['data'] == self.result_new['data']
