#coding:utf-8

from config import *
from frameUtil.get_info import get_fileresult,generate_randstr,get_loadresult
from frameUtil.rwfile import get_pwd
from random import  choice,randint
from test_login import Login
from db.sqlconn import Mysql

class Test_licenseupload():
    '''信息认证'''

    def setup_class(self):
        url = get_urls("/license/upload.html",3)
        lg = Login('13210007146')
        vls = lg.get_list()
        key = vls[0]
        print("key:",key)
        self.uid = vls[1]
        print("uid:",self.uid)
        lst = ['identity1.png','identity2.png','identity3.png','identity4.png']
        lst1 = []
        for pic in lst:
            lst1.append(get_pwd(pic))
        #fpwd = get_pwd('identity1.png')
        #print(fpwd)
        files = {'file':open(lst1[0],'rb'),'file2':open(lst1[1],'rb'),'file3':open(lst1[2],'rb'),'file4':open(lst1[3],'rb')}
        parm = get_parm()
        parm['uid'] = self.uid
        parm['key'] = key
        parm['ic_no'] = '123456789987654321'
        parm['ic_name'] = '测试者'
        self.result = get_fileresult(url,parm,files)
        print(self.result)


    def test_upload(self):
        assert self.result['status'] == 0
        #assert self.result['data'] == '上传头像成功'
        #assert 1 == 2


    def teardown_class(self):
        sql = "UPDATE 630_license set status = 3  where  uid = '%s'" % (self.uid)
        db = Mysql()
        sts = db.update(sql)
        db.dispose()