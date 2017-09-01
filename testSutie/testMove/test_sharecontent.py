#coding:utf-8

from config import *
from frameUtil.get_info import get_loadresult
from random import  choice,randint
from db.sqlconn import Mysql

class Test_sharecontent():
    #分享信息

    def setup_class(self):
        #新的接口地址
        #dm = data_manage()
        self.url_new = get_urls("/share/get-share-contents.html",3)
        self.uid = get_id()
        key = get_key()
        type = choice([1,2,3,4,7,8])
        print("type:::::",type)
        parm_new = get_parm()
        sql = "select id from 630_tour where customer_id = '%s' ORDER BY id DESC" % (self.uid)
        self.db = Mysql()
        self.ddid = self.db.getRandomOne(sql)
        print("ddid::::::",self.ddid)
        parm_new['uid'] = self.uid
        parm_new['key'] = key
        parm_new['dd_id'] = self.ddid
        parm_new['activity_id'] = 3150
        parm_new['type'] = type
        self.parm_new = parm_new
        #self.result_new = get_loadresult(self.url_new,self.parm_new)
        #print("开发票（新）:",self.result_new)
        #老的接口地址
        self.url_old = get_urls("/api/get_share_content.php",5)
        parm_old = get_parm()
        parm_old['uid'] = self.uid
        parm_old['key'] = key
        parm_old['dd_id'] = self.ddid
        parm_old['activity_id'] = 3150
        parm_old['type'] = type
        self.parm_old = parm_old
        #self.result_old = get_loadresult(url_old,parm_old)
        #print("开发票（老）:",self.result_old)


    def test_compare_result(self):
        self.result_new = get_loadresult(self.url_new,self.parm_new)
        print("分享信息（新）:",self.result_new)
        self.result_old = get_loadresult(self.url_old,self.parm_old)
        print("分享信息（老）:",self.result_old)
        assert self.result_new['status'] == self.result_old['status']
        assert self.result_new['data']['title'] == self.result_old['data']['title']
        assert self.result_new['data']['content'] == self.result_old['data']['content']
        assert self.result_new['data']['need_auth'] == self.result_old['data']['need_auth']


    def teardown_class(self):
        self.db.dispose()


