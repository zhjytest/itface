#coding:utf-8

from db.connDB import get_conn,get_cur
from random import choice
from config import set_uuid,get_uuid


class data_manage():

    def __init__(self):
        self.conn = get_conn()
        self.cur = get_cur()
        print("cur::L",self.cur)
        print("conn::L",self.conn)

    def conn_close(self):
        self.cur.close()
        self.conn.close()

    def select_query_all(self,sql):
        self.cur.execute(sql)
        data = self.cur.fetchall()
        self.conn_close()
        return data


    def select_query_one(self,sql,parm):
        self.cur.execute(sql,parm)
        data = self.cur.fetchone()
        self.conn_close()
        return data

    def select_test(self,uid):
        pass




    def select_tourddid(self,uid):
        sql = "select id from 630_tour where customer_id = '%s' ORDER BY id DESC" % (uid)
        data = self.select_query_all(sql)
        res = choice(data)[0]
        set_uuid((res))





    #update data
    #更新发票状态
    def update_invoic(self,uid,status):
        sql = ""
        if status == '1':
            sql = "update 630_invoice SET STATUS = '%s',post_company = '%s',post_num = '%s' where uid = '%s' ORDER BY id desc limit 1" % (status,'圆通快递','xxx0001',uid)
        else:
            sql = "update 630_invoice SET STATUS = '%s' where uid = '%s' ORDER BY id desc limit 1" % (status,uid)
        print("sql::::",sql)
        self.cur.execute(sql)
        self.conn.commit()
        self.cur.close()
        self.conn.close()
        #print(self.cur.fetchone())








