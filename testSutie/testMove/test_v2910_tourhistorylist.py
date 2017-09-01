#/usr/local/bin
#coding:utf-8

from config import *
from frameUtil.get_info import get_loadresult,generate_randstr
from frameUtil.rwfile import get_pwd
from random import  choice,randint

class Test_tourhistorylist():
    '''行程列表'''

    def setup_class(self):
        url = get_urls("/tour/history-list.html",3)
        key = get_key()
        uid = get_id()
        parm = get_parm()
        parm['uid'] = uid
        parm['key'] = key
        parm['action'] = 'tour_list'
        parm['offset'] = 0
        parm['limit'] = 10
        self.result = get_loadresult(url,parm)
        print(self.result)


    def test_data(self):
        types = ['已完成','已取消','已开始']
        assert self.result['status'] == 0
        nums = len(self.result['data']['dd_old']) - 1
        x = randint(0,nums)
        assert int(self.result['data']['dd_old'][x]['wd_id']) <= 1000
        assert self.result['data']['dd_old'][x]['status'] in  types
