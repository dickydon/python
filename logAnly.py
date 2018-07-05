#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql.cursors
import json
class Counter(dict):
    def __missing__(self, key):
        return 0
def generationLogConfig(phost='192.168.9.62',
                        pdb='fx_log_1',
                        puser='root',
                        ppassword='root',
                        pcharset='utf8mb4', ):
    connection = pymysql.connect(host=phost, user=puser, password=ppassword, db=pdb, charset=pcharset,
                                 cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    sql = 'select * from t_log_fairyland where player_id = 676'
    cursor.execute(sql)
    result = cursor.fetchall()
    size = len(result)
    itemNum = Counter()
    for r in result:
        js1 = json.loads(r["get_item"])
        for js in js1:
            itemNum[str(js["item_code"])] += js["item_num"]
    return itemNum
def getRead( items,phost='192.168.9.62',
                        pdb='fx_config_1',
                        puser='root',
                        ppassword='root',
                        pcharset='utf8mb4'
                       ):
    connection1 = pymysql.connect(host=phost, user=puser, password=ppassword, db=pdb, charset=pcharset,cursorclass=pymysql.cursors.DictCursor)
    cursor1 = connection1.cursor()
    for item in items:
            sql1 = 'select name from t_item where code = ' + item
            cursor1.execute(sql1)
            result1 = cursor1.fetchall()
            if 0 == len(result1):
                sql1 = 'select name from t_item_weapon where code = ' + item
                cursor1.execute(sql1)
                result1 = cursor1.fetchall()
            for r in result1:
                print(item,"\t",r["name"],"\t",items[item])
items = generationLogConfig()
getRead(items)

