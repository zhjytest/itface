#coding:utf-8

from config import *
from frameUtil.get_info import get_loadresult,generate_randstr
from frameUtil.rwfile import get_pwd
from random import  choice,randint

class Test_activitylist():
    '''当前行程信息'''

    def setup_class(self):
        url = get_urls("activity/list.html",3)
        key = get_key()
        uid = get_id()
        parm = get_parm()
        parm['uid'] = uid
        parm['key'] = key
        parm['action'] = 'list'
        self.result = get_loadresult(url,parm)
        print(self.result)


    def test_data(self):
        assert self.result['status'] == 0
        assert self.result['data'][0]['status'] == '1'
