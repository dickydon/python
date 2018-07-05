import connect
import operator
import pymysql.cursors
import json

connect = connect.generationLogConfig()
cursor = connect.cursor()
def getItemWrongData():
	sql = 'select uid from t_player_item where player_id > 0 group by uid having count(*) > 1;'
	results = cursor.execute(sql)
	results = cursor.fetchall()
	print(len(results))
	deleteId = []
	for result in results:
		sql2 = " select * from t_player_item where uid = '" + result["uid"] + "' and player_id != 0;"
		detailResults = cursor.execute(sql2);
		detailResults = cursor.fetchall();
		itemInfo = []
		for detail in detailResults:
			itemInfo.append( detail )
		if  len(itemInfo) > 1 :
			if not operator.eq(itemInfo[0]["js_str"], itemInfo[1]["js_str"]):
				print("--------------------------------")
				print(itemInfo[0]["player_id"],result["uid"],max(itemInfo[0]["id"],itemInfo[1]["id"]))
				js1 = json.loads(itemInfo[0]["js_str"])
				js2 = json.loads(itemInfo[1]["js_str"])
				a = set(js1.keys())
				b = set(js2.keys())
				c = a | b 
				isSame = True
				for  key in c :
					if  key in js1.keys() and key in js2.keys() and js1[key] == js2[key]:
						#deleteId.append(max(itemInfo[0]["id"],itemInfo[1]["id"]))
						
						continue	
					if key in js1.keys() and js1[key]:
						print("\t\tid1:",itemInfo[0]["id"],"key:" , key,"\tjs1  value: ", js1[key])	
						isSame = False
					elif key in js2.keys()and js2[key]:
						print("\t\tid2:",itemInfo[1]["id"],"key:" , key,"\tjs2 value: ",js2[key])
						isSame = False
				if isSame:
					deleteId.append(max(itemInfo[0]["id"],itemInfo[1]["id"]))
			else:
				deleteId.append(max(itemInfo[0]["id"],itemInfo[1]["id"]))
	print(set(deleteId))
				#print(itemInfo[0]["js_str"],itemInfo[1]["js_str"])

def testTable():
	sql = 'show tables;'
	results = cursor.execute(sql)
	results = cursor.fetchall()
	for result in results:
		for key in result.keys():
			sql1 = "show create table " + result[key] + ";"
			result1 = cursor.execute( sql1)
			result1 = cursor.fetchall()
			for x in result1:
				print(x['Create Table'].find("varchar"))
testTable()
