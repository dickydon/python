with open("D:\\1039_VN\\Src\\Public\\KConfigSource\\serverDone\\2\\fanren_sy_config.sql", "r" ) as f:
	while 1:
		print(f)
		lines = f.readlines(100000)
		if not lines:
			break
		for line in lines:
			print(line)
			line.replace( 'Đới Mạcht', 'nit');