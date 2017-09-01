#coding:utf-8
from config import *
from frameUtil.get_info import get_loadresult
#from testSutie.testFlow.test_flowa_addpayment import  get_pkid


class Test_selfservicepayment:
    """
        创建自助缴费单流程1
            1.进行现金支付(非保险)
    """
    #pkid = 0

    def setup_class(self):
        #1.创建自助缴费单(非保险类) ，返回pkid
        self.add_url = get_urls("/v1/workorder/jiaofei/update",1)
        self.parm = {}
        mobile = get_mobile()   #获取用户手机号
        uid =  get_id()        #获取用户uid
        types = [1,2,3,4,5,6,8]
        #=====================
        self.parm['orderid'] = get_pkid()
        self.parm['status'] = 4
        self.result = get_loadresult(self.add_url,self.parm)
        print(self.result)
        #self.pkid = self.result['data']['pkid']
        #set_pkid(self.pkid)

        #2.通过


    def test_flow_payment(self):
        assert self.result['msg'] == '请求成功'

