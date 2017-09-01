#coding:utf-8

from config import *
from frameUtil.get_info import get_loadresult,generate_randstr
from frameUtil.rwfile import get_pwd
from random import  choice,randint

class Test_activitycur():
    '''当前活动信息，banner页进入'''

    def setup_class(self):
        url = get_urls("/activity/cur.html",3)
        key = get_key()
        uid = get_id()
        parm = get_parm()
        parm['uid'] = uid
        parm['key'] = key
        parm['action'] = 'cur'
        parm['city_id'] = 1
        self.result = get_loadresult(url,parm)
        print(self.result)


    def test_data(self):
        assert self.result['status'] == 0
        assert self.result['data'][0]['h5_url'] != None
        assert self.result['data'][0]['title'] != None
        assert '1'  in self.result['data'][0]['city_id']
        #assert 1 == 2
