#!/usr/bin/python
#coding:utf-8
import os

import pytest
from test_login import Login

lg = Login('15810553242')
lg.get_info_new()

suite = "part"    #匹配执行的策略
match = ['v2910','v3000']
dpath = 'testSutie/testMove/'
#pytest.main("testSutie/ -q --html=a.html")
lstone = ["testSutie/testMove/test_v3000_choosecar.py"]
lst = []
flist = os.listdir(dpath)
nums = len(match)
for n in range(nums):
    for fname in flist:
        if match[n] in fname:
            lst.append(os.path.join(dpath,fname))

if suite == "all":
    pytest.main("testSutie/")
elif suite == "case":
    pytest.main("testSutie/testMove/")
elif suite == "part":
    pytest.main(lst)
elif suite == "one":
    pytest.main(lstone)
else:
    pass




