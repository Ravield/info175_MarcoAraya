cenit = "cenit"
polar = "polar"
cad = raw_input("Palabra a encriptar: ")
for i in range(len(cad)):
	if cad[i] in polar:
		print cenit[polar.find(cad[i])],	
	elif cad[i] in cenit:
		print polar[cenit.find(cad[i])],
	else:
		print cad[i],
		