


#Trabajo Práctico 1

import random, os

#1)

array=[0]*20
array2=[0]*20

#Producto Escalar: a1(x)*a2(x) + a1(x)*a2(x) + (...)

def load_Array(array,array2):
    for x in range(20): #Se itera un ciclo de 250 iteraciones
        array[x]=random.randint(1,12)
        array2[x]=random.randint(1,12)

#Muestra por pantalla del vector
def display_Array(array,array2):
    for x in range(20):
        print(array[x], end=" ")
        print(array2[x], end=" ")

def scalar_Product(array,array2):
    scaleprod=[0]*2000
    sigma=scaleprod[0]
    for x in range(20):
        scaleprod[x]=array[x]*array2[x]
        
def main_Menu():
    print("***MENU PRINCIPAL***")
    print()
    print("1. Cargar números.")
    print("2. Mostrar por pantalla.")
    print("3. Obtener el producto escalar.")
    print("0. Salir.")
    print()

def buttons(opcion):
    if opcion==1:
        load_Array(array,array2)  
        print("Se han cargado exitosamente")
    elif opcion==2:
        display_Array(array,array2)   
        print()
        print("Se han cargado exitosamente")
    #elif opcion==3:
        #####

opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=int(input("Seleccione una opción (1-3): "))
    buttons(opcion)
    input("Presione Inter para continuar: ")