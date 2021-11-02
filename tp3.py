


#Trabajo práctico 3

from pyrecord import Record
import numpy as np, os, random

#1)

reg=Record.create_type("reg",
"docket",
"name",
"surname",
"notes",
docket=0,
name="",
surname="",
notes=0)

record=reg

recay=np.array([record]*10)

def load(array):
    numero=1
    nodes=np.array([0]*3)
    for x in range(len(array)):
        array[x]=reg()
        array[x].docket=array[x].docket+numero
        numero=numero+100
        array[x].notes=array[x].notes+nodes
        array[x].name=input("Por favor, ingrese un nombre: ")
        array[x].surname=input("Por favor, ingrese un apellido: ")
        array[x].notes[0]=int(input("Por favor, ingrese la nota 1: "))
        array[x].notes[1]=int(input("Por favor, ingrese la nota 2: "))
        array[x].notes[2]=int(input("Por favor, ingrese la nota 3: "))


def average(array,posicion):
    suma=0
    condicion=""
    for j in range(3):
        suma=suma+array[posicion].notes[j]
    promedio=suma/3

    if promedio>=7:
        condicion="Promovido"
    elif promedio>=4 and promedio<7:
        condicion="Regular"
    else:
        condicion="Libre"


    return promedio,condicion


def display(array):
    posicion=0
    for x in range(len(array)):
        promedio,condicion=average(recay,posicion)
        print(array[x].docket,array[x].name,array[x].surname,promedio,condicion)
        posicion=posicion+1


load(recay)
display(recay)
        

