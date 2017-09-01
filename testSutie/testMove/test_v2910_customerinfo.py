#coding:utf-8

from config import *
from frameUtil.get_info import get_loadresult,generate_randstr
from frameUtil.rwfile import get_pwd
from random import  choice,randint

class Test_customerinfo():
    '''基本信息,消息'''

    def setup_class(self):
        self.url = get_urls("/customer/info.html",3)
        key = get_key()
        uid = get_id()
        self.parm = get_parm()
        self.parm['uid'] = uid
        self.parm['key'] = key



    def test_a_customer(self):
        self.parm['type'] = 'user'
        result = get_loadresult(self.url,self.parm)
        print(result)
        assert result['status'] == 0
        assert result['data']['gender'] == 3
        assert result['data']['mobile'] == get_mobile()


    def test_b_unreadmsg(self):
        self.parm['type'] = 'msg_unread'
        result = get_loadresult(self.url,self.parm)
        print(result)
        assert int(result['data']['msg_unread']) >= 0

    def test_c_unreadact(self):
        self.parm['type'] = 'act_unread'
        result = get_loadresult(self.url,self.parm)
        print(result)
        assert result['data']['act_unread'] == '0'


    def test_d_msg(self):
        self.parm['type'] = 'msg'
        result = get_loadresult(self.url,self.parm)
        print(result)
        nums = len(result['data']) - 1
        print("nums:",nums)
        index = randint(0,nums)
        assert result['data'][index]['type'] == '系统消息'
        assert result['data'][index]['msg'] != ""
        assert result['data'][index]['status'] == '1'

    def test_e_coupon(self):
        self.parm['type'] = 'coupon'
        result = get_loadresult(self.url,self.parm)
        print(result)
        nums = len(result['data'])
        print("nums:",nums)
        if nums > 0:
            assert '有效期' in result['data'][0]['description']
            assert '每个行程只能使用一张' in result['data'][0]['description']
            assert '不能与其他优惠同享' in result['data'][0]['description']
            assert result['data'][0]['money'] == '10'
            assert result['data'][0]['status'] == '0'