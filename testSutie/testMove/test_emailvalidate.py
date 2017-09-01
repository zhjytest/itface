#coding:utf-8

from config import *
from frameUtil.get_info import get_loadresult,generate_randstr
from random import  choice,randint


class Test_emailvalidate():


    def setup_class(self):
        #新的接口地址
        self.url_new = get_urls("/email-validate/send.html",3)
        self.uid = get_id()
        key = get_key()
        self.name = generate_randstr()
        parm_new = get_parm()
        parm_new['uid'] = self.uid
        parm_new['key'] = key
        parm_new['email'] = 'zhangjiangyu@yiduyongche.com'
        self.parm_new = parm_new
        #self.result_new = get_loadresult(self.url_new,self.parm_new)
        #print("开发票（新）:",self.result_new)


    def test_compare_result(self):
        self.result_new = get_loadresult(self.url_new,self.parm_new)
        print("绑定邮箱后:",self.result_new)
        msg = ['邮件已经发送 !','邮件发送成功,请登录邮箱确认邮件 !','邮箱已被其他一度账号绑定 !']
        assert self.result_new['msg'] in msg










