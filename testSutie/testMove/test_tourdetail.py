#coding:utf-8

from config import *
from frameUtil.get_info import get_loadresult
from random import  choice,randint
from db.sqlconn import Mysql

class Test_tourdetail():


    def setup_class(self):
        #新的接口地址
        #dm = data_manage()
        self.url_new = get_urls("/tour/detail.html",3)
        self.uid = get_id()
        key = get_key()
        parm_new = get_parm()
        sql = "select id from 630_tour where customer_id = '%s' ORDER BY id DESC" % (self.uid)
        self.db = Mysql()
        self.ddid = self.db.getRandomOne(sql)
        print("ddid::::::",self.ddid)
        parm_new['uid'] = self.uid
        parm_new['key'] = key
        parm_new['ddid'] = self.ddid
        self.parm_new = parm_new
        #self.result_new = get_loadresult(self.url_new,self.parm_new)
        #print("开发票（新）:",self.result_new)
        #老的接口地址
        self.url_old = get_urls("/api/use_car.php",5)
        parm_old = get_parm()
        parm_old['uid'] = self.uid
        parm_old['key'] = key
        parm_old['ddid'] = self.ddid
        parm_old['action'] = 'tour_detail'
        self.parm_old = parm_old
        #self.result_old = get_loadresult(url_old,parm_old)
        #print("开发票（老）:",self.result_old)


    def test_compare_result(self):
        self.result_new = get_loadresult(self.url_new,self.parm_new)
        print("历史行程详情（新）:",self.result_new)
        self.result_old = get_loadresult(self.url_old,self.parm_old)
        print("历史行程详情（老）:",self.result_old)
        assert self.result_new['status'] == self.result_old['status']
        assert float(self.result_new['data']['dyn_price']) == float(self.result_old['data']['dyn_price'])
        assert float(self.result_new['data']['youhui'])  == float(self.result_old['data']['youhui'])
        if self.result_old['data']['youhui_yuee'] == "":
            assert float(self.result_new['data']['youhui_yuee']) == 0.0
        else:
            assert float(self.result_new['data']['youhui_yuee']) == float(self.result_old['data']['youhui_yuee'])
        assert self.result_new['data']['wd_image'] == self.result_old['data']['wd_image']
        assert self.result_new['data']['distance'] == self.result_old['data']['distance']
        assert self.result_new['data']['che_photo'] == self.result_old['data']['che_photo']
        assert self.result_new['data']['status'] == self.result_old['data']['status']
        assert self.result_new['data']['accident_total'] == self.result_old['data']['accident_total']
        assert self.result_new['data']['cancel_time'] == self.result_old['data']['cancel_time']
        assert self.result_new['data']['shewei'] == self.result_old['data']['shewei']
        assert self.result_new['data']['wz_num'] == self.result_old['data']['wz_num']
        assert self.result_new['data']['provider'] == self.result_old['data']['provider']
        assert self.result_new['data']['cancel_reason'] == self.result_old['data']['cancel_reason']
        assert self.result_new['data']['youhui_coupon'] == self.result_old['data']['youhui_coupon']
        assert self.result_new['data']['comment_total'] == self.result_old['data']['comment_total']
        assert self.result_new['data']['yd_time'] == self.result_old['data']['yd_time']
        assert self.result_new['data']['discount_value'] == self.result_old['data']['discount_value']
        assert self.result_new['data']['price_min'] == self.result_old['data']['price_min']
        assert self.result_new['data']['car_begin_time'] == self.result_old['data']['car_begin_time']
        assert self.result_new['data']['cw_bianhao'] == self.result_old['data']['cw_bianhao']
        assert self.result_new['data']['charge_total'] == self.result_old['data']['charge_total']
        #assert self.result_new['data']['dd_yd_fee'] == self.result_old['data']['dd_yd_fee']
        assert self.result_new['data']['syh_wd_addr'] == self.result_old['data']['syh_wd_addr']
        assert self.result_new['data']['cw_floor'] == self.result_old['data']['cw_floor']
        assert self.result_new['data']['feedback_car_total'] == self.result_old['data']['feedback_car_total']
        assert self.result_new['data']['total_time'] == self.result_old['data']['total_time']
        assert self.result_new['data']['finish_time'] == self.result_old['data']['finish_time']
        assert self.result_new['data']['hongbao_flag'] == self.result_old['data']['hongbao_flag']
        assert self.result_new['data']['price_km'] == self.result_old['data']['price_km']
        #assert self.result_new['data']['bjmp_price'] == self.result_old['data']['bjmp_price']
        assert int(self.result_new['data']['car_camera']) == self.result_old['data']['car_camera']
        assert self.result_new['data']['type'] == self.result_old['data']['type']
        assert self.result_new['data']['charge_distance'] == self.result_old['data']['charge_distance']
        assert self.result_new['data']['charge_time'] == self.result_old['data']['charge_time']
        assert self.result_new['data']['dd_park_fee'] == self.result_old['data']['dd_park_fee']
        assert self.result_new['data']['jiaofei_time'] == self.result_old['data']['jiaofei_time']
        assert self.result_new['data']['addr'] == self.result_old['data']['addr']
        assert self.result_new['data']['charge_actual'] == self.result_old['data']['charge_actual']
        assert self.result_new['data']['discount_type'] == self.result_old['data']['discount_type']
        assert self.result_new['data']['breakdown_total'] == self.result_old['data']['breakdown_total']


    def teardown_class(self):
        self.db.dispose()









