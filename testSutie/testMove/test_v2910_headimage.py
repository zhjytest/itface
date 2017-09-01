#coding:utf-8

from config import *
from frameUtil.get_info import get_fileresult,generate_randstr
from frameUtil.rwfile import get_pwd
from random import  choice,randint

class Test_headimage():
    '''头像上传'''

    def setup_class(self):
        url = get_urls("/upload/head-image.html",3)
        key = get_key()
        uid = get_id()
        fpwd = get_pwd('test.jpg')
        print(fpwd)
        files = {'file':open(fpwd,'rb')}
        parm = get_parm()
        parm['uid'] = uid
        parm['key'] = key
        self.result = get_fileresult(url,parm,files)
        print(self.result)


    def test_upload(self):
        assert self.result['status'] == 0
        assert self.result['data'] == '上传头像成功'
        #assert 1 == 2
