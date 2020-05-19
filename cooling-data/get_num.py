f = open("test.out", "r")
i = 0
for x in f:
	i = i + 1
	
	if i % 2 != 0:
		if "frequency" in x:
			i = i + 1
		else:
			print(x[5:9])
