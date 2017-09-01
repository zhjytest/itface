import random

from config import *
from frameUtil.get_info import get_loadresult



class Test_paymentpay:
    """
    version:2.9.2
    author:zhangjiangyu
    time:2017.06.09
    功能:自主缴费支付
    """
    def setup_class(self):
        #self.url = "http://test.yiduyongche.com/zzjf/self-service-payment-list.html"
        self.url = get_urls("/zzjf/self-service-payment-pay.html")
        parm = get_parm()
        uid = get_id()
        key = get_key()
        parm['id'] = get_pkid()
        parm['uid'] = uid
        parm['key'] = key
        self.method =  random.choice(("zfb",'wx'))
        parm['method'] = self.method
        self.parm = parm
        self.result = get_loadresult(self.url,self.parm)
        print(self.result)
        self.data = self.result['data']
        print(self.data)



    def teardown_class(self):
        pass

    def test_method(self):
        if self.data:
            assert self.data['pay_method'] == self.method
        else:
            print("该id不是待缴费状态")




