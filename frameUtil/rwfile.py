#coding:utf-8

import os

bs = 'testSutie'

def get_pwd(filename,tls='tools'):
    dirpwd = os.getcwd().split(bs)[0]
    dirname =  os.path.join(dirpwd,tls)
    flname = os.path.join(dirname,filename)
    print(flname)
    return flname