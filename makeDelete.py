import os
import json
path="E:\\workspace\\python\\old\\"
files=os.listdir(path)
for file in files:
	with open(path+file, "r" ) as f:
		print(path+file)
		s = json.load(f)
		for key in s.keys():
			for server in s[key]:
				if server["proxy"] == 90:
					sqlString = "INSERT INTO `t_operation_online` (`cmd_type`, `cmd_level`, `oper_value`, `oper_value_ex`) VALUES ( '2007', '2', '" + str(server["server"]) + "', '" + str(server["proxy"]) + "');"
					print(sqlString)
				#else:
				#	pass
					#print(server["server"])