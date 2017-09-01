#coding:utf-8
import os

import pytest

from frameUtil.Getconfig import get_suite,get_flowcase
from test_login import Login

lg = Login('15810553242')
lg.get_info()
#gc = Getconfig()
suite = get_suite()
cases = get_flowcase()
print(cases)
#print("casetype:",type(cases))
case_name = cases.split(',')

caselst = "testSutie/"
flist = os.listdir(caselst)
del flist[0]
del flist[-1]
#del flist[-2]
for index,name in enumerate(flist):
    #print("name=====",name)
    flist[index] = caselst + name

lst = []
for name in case_name:
        pathfile  = caselst + name
        lst.append(pathfile)
        try:
            flist.remove(pathfile)
        except Exception as e:
            print("已删除")

if suite == "all":
    pytest.main(lst)
    pytest.main(flist)
    #print("filelist===============",flist)
elif suite == "flow":
    #report = "--html=log.html"
    pytest.main(lst)
elif suite == "part":
    pass
else:
    pass

#pytest.main("testSutie/")

#lst = []



