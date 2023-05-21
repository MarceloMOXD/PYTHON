from tkinter import *
from tkinter import messagebox
from math import sqrt
import re

ventana = Tk()
ventana.title("Calculadora Pedorra")
ventana.geometry("300x450")
ventana.config(bg="gray22")
operacion=StringVar(value="")
resultado_pantalla = StringVar()

def numeros(num):
    resultado_pantalla.set("")
    operacion_actual = operacion.get()
    operacion.set(operacion_actual + num)
    
def simbolos(simbolo):
    resultado_pantalla.set("")
    operacion_actual = operacion.get()
    if not operacion_actual.endswith(simbolo):
        operacion.set(operacion_actual + simbolo)

def borrar_uno(operacion):
    resultado_pantalla.set("")
    operacion_actual = operacion.get()
    operacion.set(operacion_actual[:-1])
    
def borrar_parcial(operacion):
    resultado_pantalla.set("")
    operacion_actual = operacion.get()
    simbolos = re.findall(r'[+\-*/]', operacion_actual)
    if simbolos:
        ultimo_simbolo = simbolos[-1]
        operacion.set(operacion_actual[:operacion_actual.rindex(ultimo_simbolo)])
        
def borrar_todo():
    operacion.set("")
    resultado_pantalla.set("")

def resultado():
    expresion = operacion.get()
    try:
        resultado = eval(expresion)
        resultado_pantalla.set("="+str(resultado))
    except(SyntaxError, TypeError):
        resultado_pantalla.set("SyntaxError")
        operacion.set("")
        
marca_calculadora = Label(ventana,text="Chasio",font="Courier 12",bg="gray22",fg="snow").place(x=16,y=1,width=264)
pantalla = Label(ventana,bg="honeydew2").place(x=16,y=20,width=264,height=66)
boton_e = Button(ventana, text= "e",font="15",bg="gray22",fg="snow",command = lambda: numeros("(2.71828)")).place(x=16,y=99,width=50,height=50)
boton_π = Button(ventana, text= "π",font="15",bg="gray22",fg="snow",command = lambda: numeros("(3.1416)")).place(x=70,y=99,width=50,height=50)
boton_exponente = Button(ventana, text= "E",font="15",bg="gray22",fg="snow",command= lambda: simbolos("**")).place(x=124,y=99,width=50,height=50)
boton_parentesis_abrir = Button(ventana, text= "(",font="15",bg="gray22",fg="snow",command = lambda: numeros("(")).place(x=178,y=99,width=50,height=50)
boton_parentesis_cerrar = Button(ventana, text= ")",font="15",bg="gray22",fg="snow",command = lambda: numeros(")")).place(x=232,y=99,width=50,height=50)

boton_borrar_uno = Button(ventana, text= "<-",font="15",bg="red4",fg="snow",command= lambda: borrar_uno(operacion)).place(x=16,y=153,width=50,height=50)
boton_borrar_parcial = Button(ventana, text= "CE",font="15",bg="gray22",fg="snow",command= lambda: borrar_parcial(operacion)).place(x=70,y=153,width=50,height=50)
boton_c = Button(ventana, text= "C",font="15",bg="gray22",fg="snow",command=borrar_todo).place(x=124,y=153,width=50,height=50)
boton_simbolo = Button(ventana, text= "+-",font="15",bg="gray22",fg="snow",command= lambda: numeros("(-")).place(x=178,y=153,width=50,height=50)
boton_raiz = Button(ventana, text= "sqr",font="15",bg="gray22",fg="snow",command = lambda: numeros("sqrt(")).place(x=232,y=153,width=50,height=50)

boton_siete = Button(ventana, text= "7",font="15",bg="gray26",fg="snow",command = lambda: numeros("7")).place(x=16,y=207,width=50,height=50)
boton_ocho = Button(ventana, text= "8",font="15",bg="gray26",fg="snow",command= lambda: numeros("8")).place(x=70,y=207,width=50,height=50)
boton_nueve = Button(ventana, text= "9",font="15",bg="gray26",fg="snow",command= lambda: numeros("9")).place(x=124,y=207,width=50,height=50)
boton_divi = Button(ventana, text= "/",font="15",bg="gray22",fg="snow",command= lambda: simbolos("/")).place(x=178,y=207,width=50,height=50)
boton_porcentaje = Button(ventana, text= "%",font="15",bg="gray22",fg="snow",command = lambda: simbolos("%")).place(x=232,y=207,width=50,height=50)

boton_cuatro = Button(ventana, text= "4",font="15",bg="gray26",fg="snow",command= lambda: numeros("4")).place(x=16,y=261,width=50,height=50)
boton_cinco = Button(ventana, text= "5",font="15",bg="gray26",fg="snow",command= lambda: numeros("5")).place(x=70,y=261,width=50,height=50)
boton_seis = Button(ventana, text= "6",font="15",bg="gray26",fg="snow",command= lambda: numeros("6")).place(x=124,y=261,width=50,height=50)
boton_multi = Button(ventana, text= "x",font="15",bg="gray22",fg="snow",command= lambda: simbolos("*")).place(x=178,y=261,width=50,height=50)
boton_inverso = Button(ventana, text= "1/x",font="15",bg="gray22",fg="snow",command= lambda: numeros("1/")).place(x=232,y=261,width=50,height=50)

boton_uno = Button(ventana, text= "1",font="15",bg="gray26",fg="snow",command = lambda: numeros("1")).place(x=16,y=315,width=50,height=50)
boton_dos = Button(ventana, text= "2",font="15",bg="gray26",fg="snow",command= lambda: numeros("2")).place(x=70,y=315,width=50,height=50)
boton_tres = Button(ventana, text= "3",font="15",bg="gray26",fg="snow",command= lambda: numeros("3")).place(x=124,y=315,width=50,height=50)
boton_resta = Button(ventana, text= "-",font="15",bg="gray22",fg="snow",command= lambda: numeros("-")).place(x=178,y=315,width=50,height=50)
boton_igual = Button(ventana, text= "=",font="15",bg="RoyalBlue1",fg="snow",command=resultado).place(x=232,y=315,width=50,height=104)

boton_cero = Button(ventana, text= "0",font="15",bg="gray26",fg="snow",command= lambda: numeros("0")).place(x=16,y=369,width=104,height=50)
boton_punto = Button(ventana, text= ".",font="15",bg="gray22",fg="snow",command= lambda: simbolos(".")).place(x=124,y=369,width=50,height=50)
boton_suma = Button(ventana, text= "+",font="15",bg="gray22",fg="snow",command= lambda: simbolos("+")).place(x=178,y=369,width=50,height=50)
label_operaciones = Label(ventana,textvariable=operacion,bg="honeydew2").place(x=17,y=21)
label_resultado = Label(ventana,textvariable=resultado_pantalla,bg="honeydew2").place(x=17,y=65)

ventana.mainloop()