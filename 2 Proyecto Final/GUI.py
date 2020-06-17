# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 10:18:41 2020

@author: DAVIIIIII
"""
from tkinter import *
from numpy import *
import simplex_all as Simplex
app = Tk()

app.geometry("1000x800")

equi = [0 for columna in range(0,6)]
for i in range(6):
    equi[i] = StringVar()
    equi[i].set("<")
datos = [ [0 for columna in range(0,7)] for fila in range (0,5)]
for i in range(0,5): 
    for j in range(0,7):
        if j==5:
            datos[i][j]=OptionMenu(app, equi[i], "<","=")
        else:
            datos[i][j]= Entry(app)



Mylabel1 = Label(app, text="CALCULADORA SIMPLEX") #Title
Mylabel1.pack()

CASE = StringVar()
CASE.set("min")

NVA = StringVar()
NVA.set("2") 

NRE = StringVar()
NRE.set("1")

label0 = Label(app, text="ingrese el caso a evaluar")
label0.pack()
TCASE =  OptionMenu(app, CASE, "min", "max")#combobox tipo de funcion
TCASE.pack()
label1 = Label(app, text="ingrese el numero de variables")
label1.pack()
NVariab =  OptionMenu(app, NVA, "2", "3","4")#combobox numero de variables
NVariab.pack()
label2 = Label(app, text="ingrese el numero de restriccioens")
label2.pack()
NRestric = OptionMenu(app, NRE, "1", "2", "3","4")#combobox numero de restricciones
NRestric.pack()


def Llamado():
    C=CASE.get()
    E=NRE.get()
    A=NVA.get()
    definirFO(C,E, A)
def llamadoLee():
    C=CASE.get()
    E=NRE.get()
    A=NVA.get()
    c,b,equ,A = leer(C,E, A)
    opti_x,z = Simplex.main(c,b,equ,A)
    v = " Solución Optima: x =", opti_x, ", z =", z
    label = Label(app, text=v).pack()
    
    #labelFinal = Label(app, text="Solucion optima x= " + opti_x + ",z= " + z)
    #labelFinal.pack()
    
    
def definirFO(TC,RE,VA): #define la interfaz que se va a utilizar para la toma de datos
    Boton.pack_forget()
    label0.pack_forget()
    label1.pack_forget()
    label2.pack_forget()
    TCASE.pack_forget()
    NVariab.pack_forget()
    NRestric.pack_forget()
    VA=int(VA)
    RE=int(RE)
    labelVFO = Label(app, text="Coeficientes funcion objetivo:  "+TC+":")
    labelVFO.pack()
    for i in range (VA):
        datos[i][0].pack()
    labelVR = Label(app, text="Coeficientes restricciones:")
    labelVR.pack()
    
  
    for i in range(0,RE):
        for j in range(0,VA):
            datos[i+1][j+1].pack()
        datos[i+1][5].pack()
        datos[i+1][6].pack()
        l = Label(app, text="",pady=5).pack()
    BotonS.pack()  
          
            
def leer(TC,RE,VA):
    c=""
    equ=""
    b=""
    A=""
    VA=int(VA)
    RE=int(RE)
    for i in range (VA):
        c = c + datos[i][0].get() + " "
    for i in range(0,RE):
        equ = equ + equi[i].get() + " "
        b= b + datos[i+1][6].get() + " "
        
    for i in range(0,RE):
        for j in range(0,VA):
            A= A + datos[i+1][j+1].get() + " "
    print(c,b,equ,A)
    return c,b,equ,A

    
  
    for i in range(0,RE):
        for j in range(0,VA):
            datos[i+1][j+1].pack_forget()
        datos[i+1][5].pack_forget()
        datos[i+1][6].pack_forget()
    BotonS.pack_forget()
    BotonV.pack_forget()
    
BotonS = Button(app, text="calcularSimplex", pady=10, command=llamadoLee) #boton para ejecutar simplex
Boton = Button(app, text="Generar", pady=10, command=Llamado) #boton para constuir la funcion objetivo con sus restrricciones
Boton.pack()


app.mainloop()



