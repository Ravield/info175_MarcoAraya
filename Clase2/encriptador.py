from Tkinter import *
import string

window = Tk()
window.title("Encripatador")

window.geometry("500x500")

def encriptar(text,restext,opc):
    if opc == 1:
        restext.set(encrypt(text,op2.get()))
        print text
    elif opc == 2:
        restext.set(cenitpolar(text))
        print text

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

def cenitpolar(palabra):
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
        
S = Scrollbar(window)
T = Text(window, height= 10,width=60)
S.place(x = 450 , y = 100)
T.place(x = 20 , y = 45)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)

text1=T.get('1.0','end-1c')
resultadoEncript=StringVar()

op=IntVar()
op2=StringVar()

etiqueta1=Label(window,text="ingrese texto")
etiqueta1.place(x=20,y=20)

cesar = Radiobutton(window,text="cesar",value=1,variable=op)
cesar.place(x=50,y=210)

cenpol = Radiobutton(window,text="cenit-polar",value=2,variable=op)
cenpol.place(x=150,y=210)

etiqueta2=Label(window,text="Especifique el salto para encriptacion cesar: ")
etiqueta2.place(x=20,y=230)

barra=Spinbox(window,from_=0,to=26,textvariable=op2)
barra.place(x=300,y=230)

respuesta=Label(window,textvariable=resultadoEncript)
respuesta.place(x=20,y=350)

boton1 = Button(window,text='Encriptar',command=lambda:encriptar(text1,resultadoEncript,op))
boton1.place(x=210,y=450)


window.mainloop()
