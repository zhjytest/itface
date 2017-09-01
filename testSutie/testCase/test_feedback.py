#coding:utf-8
from config import *
from frameUtil.get_info import get_loadresult
import random

class Test_feedback:
    """
            version:2.9.2
            author:zhangjiangyu
            time:2017.06.09
            功能：意见反馈列表
    """

    def setup_class(self):
        self.url = get_urls("/feedbacknew/reply-log.html")
        parm = get_parm()
        #uid = get_id()
        #key = get_key()
        parm["id"] = 517
        self.parm = parm
        self.result = get_loadresult(self.url,self.parm)



    def teardown_class(self):
        pass

    def test_feedback(self):
        name = ['车辆问题','网点问题','App问题','体验问题','咨询','其他']
        lst = self.result['data']
        num = len(lst)
        index = random.randint(1,num-1)
        assert lst[index]['name'] in name



