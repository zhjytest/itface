#coding:utf-8

import requests
import json
from config import set_key,set_uid,set_mobile,get_urls,get_parm
from frameUtil.get_info import get_loadresult

class Login():
    addr = "http://123.57.217.108/api/register.php"
    phone = ''
    def __init__(self):
        #self.phone = self.phone
        self.url = get_urls("/login/code.html",3)
        parm = get_parm()
        parm['phone'] = self.phone
        #parm = {'phone':self.phone,'action':'register','type':'login'}
        self.parm = parm
        self.r = get_loadresult(self.url,self.parm)


    def get_randstr(self):
        status = self.r['status']
        if status == 0:
            randstr = self.r['data']['randstr']
        else:
            randstr = self.r['msg']
        return randstr

    def get_info(self):
        randstr = self.get_randstr()
        parm = {'phone':self.phone,'action':'check_code','check_code':'2310','randstr':randstr}
        self.rlt = requests.post(self.addr,parm)
        result = self.rlt.text
        load_result = json.loads(result)
        #print(load_result)
        status = load_result['status']
        if status == 0:
            key = load_result['data']['check_key']
            id = load_result['data']['id']
            mobile = load_result['data']['mobile']
        else:
            key = load_result['msg']
        set_key(key)
        set_uid(id)
        set_mobile(mobile)
        #return key

    def get_info_new(self):
        randstr = self.get_randstr()
        ver_url = get_urls("/login/verify.html",3)
        parm = get_parm()
        parm['code'] = 2310
        parm['phone'] = self.phone
        result_new = get_loadresult(ver_url,parm)
        status = result_new['status']
        if status == 0:
            key = result_new['data']['check_key']
            id = result_new['data']['id']
            mobile = result_new['data']['mobile']
        else:
            key = result_new['msg']
        set_key(key)
        set_uid(id)
        set_mobile(mobile)

    def get_list(self):
        randstr = self.get_randstr()
        ver_url = get_urls("/login/verify.html",3)
        parm = get_parm()
        parm['code'] = 2310
        parm['phone'] = self.phone
        result_new = get_loadresult(ver_url,parm)
        key = result_new['data']['check_key']
        uid = result_new['data']['id']
        lst = []
        lst.append(key)
        lst.append(uid)
        print(lst)
        return lst




if __name__ == '__main__':
    lg = Login('15810553242')
    #print(lg.get_headers())
    print(lg.get_key())
    #print(lg.get_cookies())
