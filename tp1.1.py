



#Trabajo Práctico 1.1
import random, os

#1)

array=[0]*11


def load_Array(array):
    for x in range(len(array)): 
        array[x]=random.randint(-15,15)


def display_Array(array):
    for x in range(len(array)):
        print(array[x],end=" ")


def bubble_Dazzle(array):
    lenght=len(array)
    termino=False
    while not(termino):
        lenght=lenght-1
        termino=True
        for x in range(lenght):
            if array[x]>array[x+1]:
                array[x]=array[x]+array[x+1]
                array[x+1]=array[x]-array[x+1]
                array[x]=array[x]-array[x+1]
                termino=False

#-------------------------------------------------


#a)
def search_Repeated(array,busqueda):
    contador=0
    for x in range(len(array)):
        if busqueda==array[x]:
            contador=contador+1

    return contador

#-------------------------------------------------

#b)
def lineal_Search(array,busqueda):
    contador=0
    posicion=-1
    while contador<len(array) and posicion==-1:
        if array[contador]==busqueda:
            posicion=contador
        contador=contador+1

    return posicion
    
#-------------------------------------------------

#c)
def x(array,busqueda):
    contador=0
    elementos=0
    array2=[0]*elementos
    posicion=0
    for x in range(14): #El problema esta dentro de este ciclo
        if array[contador]==busqueda:
            elementos=elementos+1
            array2[0]=contador #Tambien se tiene que referenciar de vuelta al array2
            posicion=posicion+1

        contador=contador+1

    return array2

def binary_Search(array,busqueda):
    posicioni=0
    posicionf=len(array)-1
    termino=False
    while posicioni<=posicionf and not(termino):
        medium=(posicioni+posicionf)//2

        if busqueda==array[medium]:
            termino=True

        elif busqueda>array[medium]:
            posicioni=medium+1

        elif busqueda<array[medium]:
            posicionf=medium-1
    
    return termino




def main_Menu():
    print("***MENU PRINCIPAL***")
    print()
    print("1. Cargar números.")
    print("2. Mostrar por pantalla.")
    print("3. Ordenar.")
    print("4. Buscar por número.")
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
        bubble_Dazzle(array)
        print("Se ha ordenado exitosamente")
    elif opcion==4:
        busqueda=int(input("Buscar...: "))
        statement=search_Repeated(array,busqueda)
        print("Hay",statement,"coincidencias.")
        posicion=lineal_Search(array,busqueda)
        print("El número se encuentra en la posición",posicion)
        array2=x(array,busqueda)
        print("Las posiciones donde se encuentra el",busqueda,"son",array2)

    #elif opcion==5:
        #searchpot=binary_Search(array,busqueda)
        #if searchpot:
        #    print("El elemento SI se encuentra dentro del vector.")
        #else:
        #    print("El elemento NO se encuentra dentro del vector.")
        
    

opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=int(input("Seleccione una opción (1-3): "))
    buttons(opcion)
    input("Presione Inter para continuar: ")