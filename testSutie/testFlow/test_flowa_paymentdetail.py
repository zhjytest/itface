from config import *
from frameUtil.get_info import get_loadresult


class Test_payinsurancedetail:
    """
    version:2.9.3
    author:zhangjiangyu
    time:2017.06.07
    功能：缴费详情(除保险缴费)
    """
    def setup_class(self):
        self.url = get_urls("/zzjf/self-service-payment-detail.html")
        parm = get_parm()
        uid = get_id()
        key = get_key()
        parm['uid'] = uid
        parm['key'] = key
        parm["id"] = get_pkid()
        parm["city_id"] = 1
        parm["city"] = "北京市"
        self.parm = parm
        self.result = get_loadresult(self.url,self.parm)
        print(self.result)



    def teardown_class(self):
        pass

    def test_one_detail(self):
        type = get_type()
        dict = {1:"车辆维修费",2:'清洁费',3:'停运费',4:'恶意用车费',5:'停车费',6:'其他费用',8:'行驶本押金'}
        data = self.result['data']
        status = data['status']
        name = dict[type]
        print("name:",name)
        money = str(get_money())+".00"
        if status == 1:
            #"验证待缴费的情况"
            assert data['money'] == money
            assert data['name'] == name
            assert data['status_desc'] == "待缴费"
        elif status == 2:
            assert data['money'] == money
            assert data['name'] == name
            assert data['status_desc'] == "已缴费"
            assert data['pay_channel'] == '现金'
        else:
            print("无该ID，请查看")



