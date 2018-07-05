import pymysql.cursors

def generationLogConfig(phost='192.168.9.62',
                        pdb='sx_config_1',
                        puser='root',
                        ppassword='root',
                        pcharset='utf8mb4', ):
    connection = pymysql.connect(host=phost, user=puser, password=ppassword, db=pdb, charset=pcharset,
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection