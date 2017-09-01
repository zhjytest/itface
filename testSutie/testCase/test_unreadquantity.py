#coding:utf-8
from config import *
from frameUtil.get_info import get_loadresult
import random

class Test_unread:
    """
            version:2.9.2
            author:zhangjiangyu
            time:2017.06.09
            功能：意见反馈未读数量
    """

    def setup_class(self):
        self.url = get_urls("/feedbacknew/unread-quantity.html")
        self.parm = get_parm()
        self.result = get_loadresult(self.url,self.parm)



    def teardown_class(self):
        pass

    def test_feedback(self):
        nums = self.result['data']['opinion_unread']
        nums = int(nums)
        assert nums >= 0



