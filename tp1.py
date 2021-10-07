


#Trabajo Práctico 1

import random, os

#1)
"""
array=[0]*5
array2=[0]*5

#Producto Escalar: a1(x)*a2(x) + a1(x)*a2(x) + (...)

def load_Array(array,array2):
    for x in range(5): #Se itera un ciclo de 250 iteraciones
        array[x]=random.randint(1,12)
        array2[x]=random.randint(1,12)

#Muestra por pantalla del vector
def display_Array(array,array2):
    for x in range(5):
        print(array[x],end=" ")
    for x in range(5):
        print(array2[x],end=" ")

def scalar_Product(array,array2):
    scaleprod=[0]*5
    sigma=0 #54
    for x in range(5): #1
        scaleprod[x]=array[x]*array2[x] #45 #5 #9 45
        sigma=sigma+scaleprod[x]
    print("El producto escalar da como resultado: ",sigma) 
        
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
    elif opcion==3:
        scalar_Product(array,array2)
    

opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=int(input("Seleccione una opción (1-3): "))
    buttons(opcion)
    input("Presione Inter para continuar: ")



#2)

array=[0]*120
array2=[0]*120

def load_Array(array,array2):
    for x in range(120): 
        array[x]=random.randint(1,1000)
        array2[x]=random.randint(1,1000)


def display_Array(array,array2):
    for x in range(120):
        print(array[x],end=" ")
    for x in range(120):
        print(array2[x],end=" ")


def suma_Impares(array,array2):
    suma=0
    for x in range(120):
        if (x%2)==0:
            suma=suma+array[x]
        elif (x%2)==1:
            suma=suma+array2[x]
    print("La suma de los elementos de paridad escalar es: ",suma)


def main_Menu():
    print("***MENU PRINCIPAL***")
    print()
    print("1. Cargar números.")
    print("2. Mostrar por pantalla.")
    print("3. Hallar la suma de paridad escalar.")
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
    elif opcion==3:
        suma_Impares(array,array2)
    

opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=int(input("Seleccione una opción (1-3): "))
    buttons(opcion)
    input("Presione Inter para continuar: ")




#3)

array=[0]*5


def load_Array(array):
    for x in range(len(array)): 
        array[x]=random.randint(1,15)


def display_Array(array):
    for x in range(len(array)):
        print(array[x],end=" ")


def switcher(array):
    posicion=len(array)-1
    for x in range(len(array)-1):
        array[posicion]=array[posicion]+array[posicion-1]
        array[posicion-1]=array[posicion]-array[posicion-1]
        array[posicion]=array[posicion]-array[posicion-1]
        posicion=posicion-1



def main_Menu():
    print("***MENU PRINCIPAL***")
    print()
    print("1. Cargar números.")
    print("2. Mostrar por pantalla.")
    print("3. Desplazar los elementos a la posición derecha.")
    print("0. Salir.")
    print()

def buttons(opcion):
    if opcion==1:
        load_Array(array)  
        print("Se han cargado exitosamente")
    elif opcion==2:
        display_Array(array)   
        print()
        print("Se han cargado exitosamente")
    elif opcion==3:
        switcher(array)
        print("Se han desplazado correctamente")
        
    

opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=int(input("Seleccione una opción (1-3): "))
    buttons(opcion)
    input("Presione Inter para continuar: ")
"""

#----------------------------------------------------------------
#Ejercicios Adicionales


#1)

array=[0]*50


def load_Array(array):
    for x in range(len(array)): 
        array[x]=random.randint(-15,15)


def display_Array(array):
    for x in range(len(array)):
        print(array[x],end=" ")

def pn_Z(array):
    pos=0
    neg=0
    zer=0
    for x in range(len(array)):
        if array[x]>0:
            pos=pos+1
        elif array[x]<0:
            neg=neg+1
        else:
            zer=zer+1
    return pos,neg,zer



def main_Menu():
    print("***MENU PRINCIPAL***")
    print()
    print("1. Cargar números.")
    print("2. Mostrar por pantalla.")
    print("3. Calcular la cantidad de números negativos, positivos y ceros.")
    print("0. Salir.")
    print()

def buttons(opcion):
    if opcion==1:
        load_Array(array)  
        print("Se han cargado exitosamente")
    elif opcion==2:
        display_Array(array)   
        print()
        print("Se han cargado exitosamente")
    elif opcion==3:
        p,n,z=pn_Z(array)
        print("La cantidad de números positivos es de: ",p)
        print("La cantidad de números negativos es de: ",n)
        print("La cantidad de números iguales a cero es de: ",z)
        
    

opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=int(input("Seleccione una opción (1-3): "))
    buttons(opcion)
    input("Presione Inter para continuar: ")
