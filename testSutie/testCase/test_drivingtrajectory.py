from config import *
#from config import get_parm
#from config import get_id
from frameUtil.get_info import get_loadresult


class Test_drivingtrajectory:
    """
    version:2.9.3
    author:zhangjiangyu
    time:2017.06.06
    """
    def setup_class(self):
        #set_url("/user-tour/driving-trajectory.html")
        self.url = get_urls("/user-tour/driving-trajectory.html")
        print("url:",self.url)
        parm = get_parm()
        uid = get_id()
        key = get_key()
        parm['uid'] = uid
        parm['key'] = key
        parm["dd_id"] = 69492
        parm["city_id"] = 1
        parm["city"] = "北京市"
        self.parm = parm
        #self.r = requests.post(self.url,self.parm)
        #self.result = self.r.text
        self.result = get_loadresult(self.url,self.parm)
        #self.load_result = json.loads(self.result)



    def teardown_class(self):
        pass

    def test_driving(self):
        return_addr = self.result['data']['return_addr']
        return_name = self.result['data']['return_name']
        print(return_addr)
        assert return_addr != ""
        assert  return_name != ""



