
from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("Calculadora Operaciones Basicas")
ventana.geometry("450x296")
ventana.maxsize(450,296)
ventana.minsize(450,296)


def suma():
    numero1 = float(num1.get())
    numero2 = float(num2.get())
    resultado.set(numero1+numero2)
    signo.set("+")

def resta():
    numero1 = float(num1.get())
    numero2 = float(num2.get())
    resultado.set(numero1-numero2)
    signo.set("-")

def multi():
    numero1 = float(num1.get())
    numero2 = float(num2.get())
    resultado.set(numero1*numero2)
    signo.set("x")
    
def divi():
    numero1 = float(num1.get())
    numero2 = float(num2.get())
    if numero2 == 0:
        messagebox.showinfo(message="No se puede dividir entre 0")
    else:
        resultado.set(numero1/numero2)
    signo.set("/")

label_operaciones = LabelFrame(ventana,text="Operaciones",font="10",relief="groove",bd=3,width=390, height=90).place(x=30,y=30)
label_operadores = LabelFrame(ventana,text = "Operadores Aritmeticos",font="10",relief="groove",bd=3,width=390, height=90).place(x=30,y=150)

num1 = StringVar()
num1.set("0")
num2 = StringVar()
num2.set("0")
signo = StringVar()
resultado = StringVar()

label_numero1 = Label(label_operaciones, text= "Numero 1",font="5").place(x=41,y=60)
label_numero2 = Label(label_operaciones, text= "Numero 2",font="5").place(x=181,y=60)
label_titulo_resultado = Label(label_operaciones, text= "Resultado",font="5").place(x=316,y=60)
label_simbolo1 = Label(label_operaciones,text = "=",font="5").place(x=280,y=80)
label_signo = Label(label_operaciones,textvariable=signo,font="5").place(x=140,y=80)
label_resultado = Label(label_operaciones,textvariable=resultado).place(x=320,y=83)

ent_numero1 = Entry(label_operaciones,textvariable=num1).place(x=40,y=83,width=80)
ent_numero2 = Entry(label_operaciones,textvariable=num2).place(x=180,y=83,width=80)


boton_suma = Button(label_operadores, text= "+",font="15",command=suma).place(x=41,y=181,width=74)
boton_resta = Button(label_operadores, text= "-",font="15",command=resta).place(x=133,y=181,width=74)
boton_multi = Button(label_operadores, text= "x",font="15",command=multi).place(x=226,y=181,width=74)
boton_divi = Button(label_operadores, text= "/",font="15",command=divi).place(x=323,y=181,width=74)

ventana.mainloop()