import connect
import operator
import pymysql.cursors
import json

connect = connect.generationLogConfig()
cursor = connect.cursor()
def getAttriData():
	sql = 'select * from t_attr_add ;'
	print(sql)
	results = cursor.execute(sql)
	results = cursor.fetchall()

	for result in results:
		newsingle = ""
		attri= result["effect_js"]
		attriArray = attri.split("#")
		for attriSingle in attriArray:
			if  attriSingle:
				if len(attriSingle.split(",")) == 2:
					continue
				attriType = attriSingle.split(",")[0]
				valueType = int(attriSingle.split(",")[1])
				newType = int(attriType)
				if  valueType:
					newType = int(attriType) + 200					
				newsingle += str(newType)+","+attriSingle.split(",")[2] + "#"
		print( "replace into t_attr_add (id,effect_js, opeObj,effect_describe) value (",result["id"],",'",newsingle,"',",result["opeObj"],",'",result["effect_describe"],"');" )

getAttriData()
	