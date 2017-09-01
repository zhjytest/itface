#coding:utf-8
import requests
import json,string
from random import sample

def get_result(url,parm):
    r = requests.post(url,parm)
    result = r.text
    return result

def get_loadresult(url,parm):
    r = requests.post(url,parm)
    result = r.text
    load_result = json.loads(result)
    return load_result

def get_fileresult(url,parm,files):
    r = requests.post(url,parm,files=files)
    result = r.text
    load_result = json.loads(result)
    return load_result


def generate_randstr():
    salt = ''.join(sample(string.ascii_letters+string.digits,6))
    return salt