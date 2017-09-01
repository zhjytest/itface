#coding:utf-8

from config import *
from frameUtil.get_info import get_loadresult,generate_randstr
from random import  choice,randint


class Test_changeprofile():


    def setup_class(self):
        #新的接口地址
        self.url_new = get_urls("/customer/change-profile.html",3)
        self.uid = get_id()
        key = get_key()
        self.name = generate_randstr()
        self.type = choice([1,2,3])
        print("type:::::",self.type)
        parm_new = get_parm()
        parm_new['uid'] = self.uid
        parm_new['key'] = key
        parm_new['name'] = self.name
        parm_new['sex'] = self.type
        self.parm_new = parm_new
        #self.result_new = get_loadresult(self.url_new,self.parm_new)
        #print("开发票（新）:",self.result_new)
        #验证接口地址
        self.url_old = get_urls("/api/get_user_info.php",5)
        parm_old = get_parm()
        parm_old['uid'] = self.uid
        parm_old['key'] = key
        parm_old['type'] = 'user'
        parm_old['city'] = '北京市'
        self.parm_old = parm_old
        #self.result_old = get_loadresult(url_old,parm_old)
        #print("开发票（老）:",self.result_old)


    def test_compare_result(self):
        self.result_new = get_loadresult(self.url_new,self.parm_new)
        print("修改个人信息后:",self.result_new)
        self.result_old = get_loadresult(self.url_old,self.parm_old)
        print("通过验证的结果:",self.result_old)
        assert self.result_new['status'] == self.result_old['status']
        assert self.result_old['data']['name'] == self.name
        assert self.result_old['data']['gender']  == int(self.type)









