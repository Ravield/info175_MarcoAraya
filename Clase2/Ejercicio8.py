import string

def encrypt(palabra,N):
	p=""
	abc = string.ascii_lowercase
	abc = string.ascii_uppercase
	for char in palabra:
		if char != " ":
			index = (abc.index(char.lower()) + N) % len(abc)
			p += abc[index]
		else:
			p += char

	return p

if __name__=="__main__":
	print encrypt(raw_input("ingrese una palabra: "),int(raw_input("ingrese un numero: ")))


