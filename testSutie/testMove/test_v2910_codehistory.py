#coding:utf-8

from config import *
from frameUtil.get_info import get_loadresult,generate_randstr
from frameUtil.rwfile import get_pwd
from random import  choice,randint

class Test_codehistory():
    '''兑换历史'''

    def setup_class(self):
        url = get_urls("/code/history.html",3)
        key = get_key()
        uid = get_id()
        parm = get_parm()
        parm['uid'] = uid
        parm['key'] = key
        parm['action'] = 'list'
        self.result = get_loadresult(url,parm)
        print(self.result)


    def test_data(self):
        assert self.result['data'][0]['desc'] == '使用分享码获得优惠券'
        assert self.result['data'][0]['type'] == 'user'
        assert self.result['data'][0]['user'] == str(get_mobile())



