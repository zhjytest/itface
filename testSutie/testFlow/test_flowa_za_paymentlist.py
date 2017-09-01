import random
from config import *
from frameUtil.get_info import get_loadresult


class Test_paymentlist_after:
    """
    version:2.9.3
    author:zhangjiangyu
    time:2017.06.07
    """
    def setup_class(self):
        """
        创建自助缴费单流程1
            1.创建自助缴费单(非保险)
            2.验证缴费列表正确性
            3.通过现金进行缴费
            4.验证缴费列表的正确性
        """
        #self.url = "http://test.yiduyongche.com/zzjf/self-service-payment-list.html"
        self.url = get_urls("/zzjf/self-service-payment-list.html")
        #self.url = get_url()
        parm = get_parm()
        uid = get_id()
        key = get_key()
        parm['uid'] = uid
        parm['key'] = key
        self.parm = parm
        self.result = get_loadresult(self.url,self.parm)
        print(self.result)
        self.lst = self.result['data']
        print("=================",self.lst)


    def teardown_class(self):
        pass



    #验证新建的一条的数据
    def test_last_one(self):
        last_data = self.lst[0]
        lastmoney = get_money()
        print("lastmoney:",lastmoney)
        #money = cvtstr(lastmoney)
        #print("最后一条的钱:",money)
        print("返回的钱:",last_data['money'])
        assert float(last_data['types']) == float(get_type())
        assert float(last_data['money']) == float(lastmoney)
        assert last_data['status_desc'] == '已缴费'