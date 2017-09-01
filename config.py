#from login import Login

class global_var:
    url = ["http://test.yiduyongche.com","http://123.57.217.108:8899","http://123.57.217.108:8892","http://test_new.yiduyongche.com/","http://123.57.217.108","http://ceshi.yiduyongche.com"]
    parm = {"channel": "AppStore","wei": 39.98224485598885,"clientversion": "ios_2908","device_name": "iPhone6 Plus","jing": 116.5003987571553,"device_id": "1679ff0411106a429e0a43ae04fda9010994bd39","systemversion": "10.2"}
    #parm = {"channel": "AppStore","wei": 23.104677,"clientversion": "ios_2908","device_name": "iPhone6 Plus","jing": 113.235231,"device_id": "1679ff0411106a429e0a43ae04fda9010994bd39","systemversion": "10.2"}
    key = ""
    uid = 0
    mobile = ''
    pkid = 0
    money = 0.0
    bx_money = 0.0
    types = 0
    tourid = 0

def set_parm(parm):
    global_var.parm = parm

def get_parm():
    return global_var.parm


def set_key(key):
    global_var.key = key

def get_key():
    return global_var.key


def set_uid(id):
    global_var.uid = id

def get_id():
    return global_var.uid

def set_mobile(mobile):
    global_var.mobile = mobile

def get_mobile():
    return global_var.mobile


def set_url(urls):
    global_var.url = global_var.url + urls

def get_url():
    return global_var.url

def get_urls(url,parm=0):
    urls = global_var.url[parm] + url
    return  urls


#以下方法为新建自助缴费单使用
def set_pkid(pkid):
    global_var.pkid = pkid

def get_pkid():
    return  global_var.pkid

def set_money(money):
    global_var.money = money

def get_money():
    return global_var.money

def set_type(types):
    global_var.types = types

def get_type():
    return global_var.types


#设置保险费金额
def set_bx_money(money):
    global_var.bx_money = money

def get_bx_money():
    return global_var.bx_money


#设置数据库返回的数据
def set_uuid(tourid):
    global_var.tourid = tourid

def get_uuid():
    return global_var.tourid