#coding:utf-8
from config import *
from frameUtil.get_info import get_loadresult
import random

class Test_addfeed:
    """
            version:2.9.2
            author:zhangjiangyu
            time:2017.06.09
            功能：提交意见反馈
    """

    def setup_class(self):
        self.url = get_urls("/feedbacknew/add-feedback.html")
        uid = get_id()
        key = get_key()
        parm = get_parm()
        wttype = ["clwt","wdwt","appwt","tywt","zx","qt"]
        num = random.randint(0,len(wttype)-1)
        print(num)
        code = wttype[num]
        print(code)
        parm["uid"] = uid
        parm["key"] = key
        parm["code"] = code
        parm["content"] = "test_content"
        parm["email"] = "xxx@123.com"
        parm["city"] = "北京市"
        self.parm = parm
        print("parm:",self.parm)
        self.result = get_loadresult(self.url,self.parm)
        print(self.result)



    def teardown_class(self):
        pass

    def test_feedback(self):
        msg = self.result['msg']
        assert msg == "反馈成功"



