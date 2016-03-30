if __name__=="__main__":
	lineas = ""
	linea = raw_input("Escriba una palabra:\n")
	while linea:
		linea = linea.upper()
		linea += "\n"
		lineas += linea
		linea = raw_input("Escriba una palabra:\n")

		print lineas