def pideNum(x,y):
	if x > y:
		return x,"es mayor que ",y
	elif x < y:
		return x,"es menor que ",y
	else:
		return x,"es igual a ",y

if __name__=="__main__":
	x = input("Ingrese un numero entero ")
	y = input("Ingrese otro numero entero ")

	print(pideNum(x,y))