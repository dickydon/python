import os
import json

def getProxy( server ):
	return{
	'0':80,		# andriosHF
	'20':80,	# andriosHF
	'21':81,	# andrHF1
	'40':82,	# iosHF1
	'60':80,	# andriosHF
	'61':83,	# andrHF2
	'80':84,	# junhaiyyb
	'100':85,		# app
	'120':86,		# andrjh
	'140':93,		# yybjhz
	'160':94,		# yybjhz1
	'180':87,		# yybjhz2
	'200':88,		# yybjhz3
	'220':89,		# andrTXHD
	'240':92,		# yinhu
	'260':96,		# gy37
	'270':96,		# gy37
	'280':90,		# shoumeng
	'300':91,		# ouwan
	'320':95,		# andrzqb
	}[server]


jsonPath = "E:\\workspace\\python\\old_server.json"
with open(jsonPath, "r" ) as jf:
    d2 = json.load(jf)
    oldServer=[]
    for ele in d2:
    	for x in d2[ele]:
    		oldServer.append(x["server"])
path="E:\\workspace\\python\\now_server.txt"
with open(path, "r" ) as f:
	nowServer = []
	while 1:
		lines = f.readlines(10)
		if not lines:
			break
		for line in lines:
			line = line.split('\n')
			if len(line) == 2:
				nowServer.append( int(line[0]) )
delServer = set(oldServer) - set(nowServer)
print(delServer)
for server in delServer:
	sqlString ="INSERT INTO `t_operation_online` (`cmd_type`, `cmd_level`,  `oper_value`, `oper_value_ex`) VALUES ( '2007', '2',  '" + str(server) + "', '" + str(getProxy( str( int(server / 100) ) )) + "');"
	print(sqlString)