


#Trabajo práctico 3

from pyrecord import Record
import numpy as np, os, random

#1)

nodes=np.array([0]*3)

reg=Record.create_type("reg",
"docket",
"name",
"surname",
"notes",
docket=1,
name="",
surname="",
notes=np.array([0]*3))

record=reg

recay=np.array([record]*3)

def load(array):
    for x in range(len(array)):
        array[x]=reg()
        array[x].notes[x]=nodes()
        array[x].docket=array[x].docket+100
        array[x].name=input("Por favor, ingrese un nombre: ")
        array[x].surname=input("Por favor, ingrese un apellido: ")
        array[x].notes[0]=int(input("Por favor, ingrese la nota 1: "))
        array[x].notes[1]=int(input("Por favor, ingrese la nota 2: "))
        array[x].notes[2]=int(input("Por favor, ingrese la nota 3: "))


def average(array,posicion):
    suma=0
    condicion=""
    for j in range(len(array)):
        suma=suma+array[posicion].notes[j]
    promedio=suma/len(array)

    if promedio>=7:
        condicion="Promovido"
    elif promedio>=4 and promedio<7:
        condicion="Regular"
    else:
        condicion="Libre"


    return promedio,condicion



def display(array):
    for x in range(len(array)):
        print(array[x].docket,array[x].name,array[x].surname,
        array[x].notes[0],
        array[x].notes[1],
        array[x].notes[2])



load(recay)
display(recay)
        

