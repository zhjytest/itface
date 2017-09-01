from config import *
from frameUtil.get_info import get_loadresult
import pytest
import random


class Test_returndeposit:
    """
    version:2.9.3
    author:zhangjiangyu
    time:2017.06.07
    功能：退还押金
    """
    def setup_class(self):
        self.url = get_urls("/car/query-return-deposit.html")
        parm = get_parm()
        uid = get_id()
        key = get_key()
        parm['uid'] = uid
        parm['key'] = key
        self.parm = parm
        self.result = get_loadresult(self.url,self.parm)
        print(self.result)
        self.flag = self.result['data']['flag']
        print("flag:",self.flag)



    def teardown_class(self):
        pass

    def test_flag(self):
        assert self.flag in [4,5,6]



