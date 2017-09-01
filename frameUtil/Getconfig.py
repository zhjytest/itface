#coding:utf-8

import configparser
import os

cf = configparser.ConfigParser()
path = os.path.split(os.path.realpath(__file__))[0] + '/caseconfig.conf'
cf.read(path)

def get_suite():
    suite = cf.get('suite','run')
    print(suite)
    return suite


def get_flowcase():
    flow = cf.get('case','flow001')
    return flow

