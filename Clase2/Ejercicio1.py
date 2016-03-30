def multiplos (size):
	lista = []
	for x in range(1,size+1):
		if x % 3 == 0 and x % 7 == 0:
			lista.append(x)
	return lista

if __name__=="__main__":
	size = raw_input("ingrese numero: ") 
	print multiplos(int(size))