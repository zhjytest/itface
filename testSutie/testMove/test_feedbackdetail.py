#coding:utf-8


from config import *
from frameUtil.get_info import get_loadresult,generate_randstr,get_fileresult
from random import  choice,randint
from db.sqlconn import Mysql
from time import sleep

class Test_feedbackdetail():


    def setup_class(self):
        #新的接口地址
        #dm = data_manage()
        self.url_new = get_urls("/feed-back/upload.html",3)
        self.uid = get_id()
        self.lst = ['upload','list']
        key = get_key()
        self.content = generate_randstr()
        sql = "select id from 630_tour where customer_id = '%s' ORDER BY id DESC" % (self.uid)
        self.db = Mysql()
        self.ddid = self.db.getRandomOne(sql)
        parm_new = get_parm()
        #self.ddid = dm.select_tourddid(self.uid)
        print("ddid::::::",self.ddid)
        parm_new['uid'] = self.uid
        parm_new['key'] = key
        parm_new['order_id'] = self.ddid
        parm_new['action'] = 'upload'
        parm_new['content'] = self.content
        self.parm_new = parm_new
        print(self.parm_new)
        #老的接口地址
        # self.url_old = get_urls("/feed-back/upload.html",3)
        # parm_old = get_parm()
        # parm_old['uid'] = self.uid
        # parm_old['key'] = key
        # parm_old['order_id'] = self.ddid
        # parm_old['action'] = 'list'
        # self.parm_old = parm_old
        # print(self.parm_old)



    def test_commit(self):
        x = randint(1,10)
        files = {'file':open('d:/project/pyinterface/yditface/tools/test.jpg','rb')}
        if x == 10:
            self.result_new = get_fileresult(self.url_new,self.parm_new,files)
        else:
            self.result_new = get_loadresult(self.url_new,self.parm_new)
        print("意见反馈提交后:",self.result_new)
        assert self.result_new['status']  == 0

    def test_feedback_result(self):
        self.parm_new['action'] = 'list'
        self.result_old = get_loadresult(self.url_new,self.parm_new)
        print("意见反馈数据展示:",self.result_old)
        assert self.result_old['status']  == 0
        print("+++++++++++",self.result_old['data'][0]['pics'])
        if self.result_old['data'][0]['pics']:
            assert 'https://imgtest.yiduyongche.com/feedback/feedback' in self.result_old['data'][0]['pics'][0]
        assert self.result_old['data'][0]['order_id'] == str(self.ddid)
        assert self.result_old['data'][0]['content'] == self.content


    def teardown_class(self):
        self.db.dispose()













