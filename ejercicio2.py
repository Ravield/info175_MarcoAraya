if __name__=="__main__":
	lineas = []
	linea = raw_input("Escriba una palabra:\n")
	while linea:
		lineas.append(linea)
		linea = raw_input("Escriba una palabra:\n")

	lineas = sorted(lineas)

	print lineas