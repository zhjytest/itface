from config import *
from frameUtil.get_info import get_loadresult
#from testSutie.testFlow.test_flowa_addpayment import  get_pkid


class Test_payinsurancedetail:
    """
    version:2.9.3
    author:zhangjiangyu
    time:2017.06.07
    功能：保险缴费详情
    """
    def setup_class(self):
        self.url = get_urls("/zzjf/self-service-payment-detail-insurance.html")
        parm = get_parm()
        uid = get_id()
        key = get_key()
        id = get_pkid()
        print("id:",id)
        parm['uid'] = uid
        parm['key'] = key
        parm["id"] = id
        parm["city_id"] = 1
        parm["city"] = "北京市"
        self.parm = parm
        self.result = get_loadresult(self.url,self.parm)
        print(self.result)



    def teardown_class(self):
        pass

    def test_detail(self):
        pay_channel = ['现金','微信支付','支付宝支付']
        status_desc = ['已缴费','已退款','退款中','待缴费']
        data = self.result['data']
        print("data['pay_channel']",type(data['pay_channel']))
        if data != None:
            assert  data['pay_channel'] in pay_channel
            assert  data['status_desc'] in status_desc
        else:
            print("无该ID，请查看")



