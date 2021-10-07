



#Trabajo Práctico 1.2
import random, os

"""
#1)

array=["Auto","Casa","Garage","Jardin","Patio","Terraza"]


def display_Array(array):
    for x in range(len(array)):
        print(array[x], end=" ")

def mintomay(array):
    ordenado="No"
    for x in range(len(array)-1):
        if array[x]<array[x+1]:
            ordenado="Ordenado"
        else:
            ordenado="Desordenado"

    return ordenado 


def main_Menu():
    print("***MENU PRINCIPAL***")
    print()
    print("1. Mostrar por pantalla el vector.")
    print("2. Comprobar si esta ordenado de menor a mayor.")
    print("0. Salir.")
    print()

def buttons(opcion):
    if opcion==1:
        display_Array(array)   
        print()
        print("Se han cargado exitosamente")
    elif opcion==2:
        ordenado=mintomay(array)
        print("Se encuentra",ordenado)

opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=int(input("Seleccione una opción (1-0): "))
    buttons(opcion)
    input("Presione Inter para continuar: ")
"""

#2)

arrayp=[2,4,6,9]
arrayi=[3,7,9,11,13,15]
arrayip=arrayp+arrayi

for x in range(len(arrayip)):
    if arrayip[x]>arrayip[x+1]:
        arrayip[x]+=arrayi[x+1]
        arrayip[x+1]=arrayip[x]-arrayip[x+1]
        arrayip-=arrayip[x+1]
        print(arrayip[x])





