#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql.cursors


def generationLogConfig(phost='192.168.9.69',
                        pdb='fanren_sy_log',
                        puser='root',
                        ppassword='root',
                        pcharset='utf8mb4', ):
    connection = pymysql.connect(host=phost, user=puser, password=ppassword, db=pdb, charset=pcharset,
                                 cursorclass=pymysql.cursors.DictCursor)
    f = open('..\..\Config\log_config.json', 'wt')
    f.write('{\n')
    f.write('\t[\n')
    cursor = connection.cursor()
    sql = 'show tables;'
    cursor.execute(sql)
    result = cursor.fetchall()
    size = len(result)
    i = 1
    for r in result:
        tableName = r["Tables_in_" + pdb]
        f.write('\t\t{ "table_name": "' + tableName + '",\n')
        f.write('\t\t  "columns": {\n')
        sqlStruct = 'show columns from ' + tableName + ';'
        cursor.execute(sqlStruct)
        structRes = cursor.fetchall()
        columnsize = len(structRes)
        j = 1
        for c in structRes:
            f.write('\t\t\t  "' + str(j) + '":{\n')
            f.write('\t\t\t\t\t"col_name": "' + c["Field"] + '",\n')
            columntype = c["Type"].split('(', maxsplit=1)
            f.write('\t\t\t\t\t"type": "' + columntype[0] + '"\n')
            if columnsize == j:
                f.write('\t\t\t\t}\n')
            else:
                f.write('\t\t\t\t},\n')
            j = j + 1
        #  print( "col_name: " + c["Field"] + " type: " + c["Type"]  )
        if size == i:
            f.write('\n\t\t\t}\n\t\t}\n')
        else:
            f.write('\n\t\t\t}\n\t\t},\n')
        i = i + 1
    f.write('\t]\n')
    f.write('}')
    f.close()
    connection.close()


# ip,dbname,user,password
generationLogConfig()
