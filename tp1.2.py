



import os
#Trabajo Práctico 1.2
import random

#1)

"""
array=["Auto","Casa","Garage","Jardin","Patio","Terraza"]
####

#####

def load_Array(array):
    for x in range(len(array)): 
        array[x]=random.randint(-15,15)

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
    print("3. Mostrar por pantalla el vector #2.")
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
    elif opcion==3:
        display_Array(arrayip)
        print()
        print("Se han cargado exitosamente")



opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=int(input("Seleccione una opción (1-0): "))
    buttons(opcion)
    input("Presione Inter para continuar: ")

"""
#2)


array=[2,4,6,9]
array2=[3,7,9,11,13,15]
tamaño=len(array+array2)
array3=[0]*tamaño

def display_Array(array3):
    for x in range(len(array3)):
        print(array3[x], end=" ")


def ordering(array,array2,array3):
    posicion=0
    for x in range(len(array)):
        array3[x]=array[x]
    for j in range(len(array),tamaño):
        array3[j]=array2[posicion]
        posicion=posicion+1

        


def main_Menu():
    print("***MENU PRINCIPAL***")
    print()
    print("1. Mostrar por pantalla el vector.")
    print("2. Comprobar si esta ordenado de menor a mayor.")
    print("0. Salir.")
    print()

def buttons(opcion):
    if opcion==1:
        display_Array(array3)   
        print()
        print("Se han cargado exitosamente")
    elif opcion==2:
        ordering(array,array2,array3)

opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=int(input("Seleccione una opción (1-0): "))
    buttons(opcion)
    input("Presione Inter para continuar: ")

