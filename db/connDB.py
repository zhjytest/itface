#coding:utf-8
import pymysql
import unittest
import random

class connDB:
    host = "123.57.214.110"
    user = "mysql630"
    passwd = "YjCsXdL#@.a64L"
    db = "630ver"
    conn = pymysql.connect(host=host,user=user,passwd=passwd,db=db)
    cur = conn.cursor()


    def select_test(self,uid):
        sql = "select mobile from 630_customer where id = '%s'" % (uid)
        print(sql)
        reslt = self.cur.execute(sql)
        data = self.cur.fetchone()
        print(data[0])
        self.cur.close()
        self.conn.close()


def get_conn():
    return connDB.conn

def get_cur():
    return connDB.cur

if __name__ == "__main__":
    conndb = connDB()
    conndb.select_test(261873)


