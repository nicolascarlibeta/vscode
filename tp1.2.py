



import os
#Trabajo Práctico 1.2
import random, numpy as np


#1)

"""
array=["Auto","Casa","Garage","Jardin","Patio","Terraza"]

def load_Array(array):
    for x in range(len(array)): 
        array[x]=random.randint(-15,15)

def display_Array(array):
    for x in range(len(array)):
        print(array[x], end=" ")

def mintomay(array):
    ordenado="Ordenado"
    contador=0
    termino=False
    while contador<len(array)-1 and not(termino):
        if array[contador]>array[contador+1]:
            ordenado="Desordenado"
            termino=True
        contador=contador+1

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
        display_Array(array3)
        print()
        print("Se han cargado exitosamente")



opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=int(input("Seleccione una opción (1-0): "))
    buttons(opcion)
    input("Presione Inter para continuar: ")


#2)

#Mientras i<len(v1) and j<len(v2)			
#	if v1[x]==v2[j]: se pasa el valor, y se suma el indice de los tres vectores		
#	if v1[x]<v2[j]:		
#	v3[x]=v1[x]
#    		
#Si se cierra el ciclo, se trasladan los numeros			
#del vector	v1[0]<v2[1]		
#	Se le suman los indices si es falso, para comparar con el siguiente		
#	El vector 3 siempre suma su indice		
# 

array2=[4,9,13,25]
array=[1,3,9,14,29,30]


def display_Array(array):
    for x in range(len(array)):
        print(array[x], end=" ")


def ordering(array,array2):
    x=0
    j=0
    tamaño=len(array+array2)
    array3=np.array([0]*tamaño)
    k=-1
    while x<len(array) and j<len(array2):
        k=k+1
        if array[x]==array2[j]:
            array3[k]=array[x]
            x=x+1
            j=j+1
            
        elif array[x]<array2[j]:
            array3[k]=array[x]
            x=x+1
        else:
            array3[k]=array2[j]
            j=j+1

    def overstep(indice,longitud,posicion,vector3,vector):    
        for z in range(indice,longitud):
            posicion=posicion+1
            vector3[posicion]=vector[z]
            
    if x==len(array):
        overstep(j,len(array2),k,array3,array2)
    
    elif j==len(array2):
        overstep(x,len(array),k,array3,array)

   
    return array3



def main_Menu():
    print("***MENU PRINCIPAL***")
    print()
    print("1. Mostrar por pantalla los vectores.")
    print("2. Ordenar dentro de un vector terciario.")
    print("0. Salir.")
    print()

def buttons(opcion):
    if opcion==1:
        print("Vector #1")
        display_Array(array)
        print()
        print("Vector #2")
        display_Array(array2)   
        print()  
        print("Se han cargado exitosamente")
    elif opcion==2:
        array3=ordering(array,array2)
        print("El vector",array3,"se ha cargado exitosamente")


opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=int(input("Seleccione una opción (1-0): "))
    buttons(opcion)
    input("Presione Inter para continuar: ")

#3)

nombre=["Jacques","Martyr","Godrick","Parvati","Lorelei"]
apellido=["Perrault","Van Sant","Ginette","Singh","Williams"]

def display_Array(array,array2):
    for x in range(len(array)):
        print(array[x],array2[x])

def bublist(array,array2):
    lenght=len(array)
    termino=False
    while not(termino):
        lenght=lenght-1
        termino=True
        for x in range(lenght):
            if array[x]>array[x+1]:
                switch=array[x]
                array[x]=array[x+1]
                array[x+1]=switch
                switch2=array2[x]
                array2[x]=array2[x+1]
                array2[x+1]=switch2
                termino=False

def main_Menu():
    print("***MENU PRINCIPAL***")
    print()
    print("1. Mostrar los nombres y apellidos.")
    print("2. Ordenar el listado por apellido.")
    print("0. Salir.")
    print()

def buttons(opcion):
    if opcion==1:
        print("Apellidos","Nombres")
        display_Array(apellido,nombre)
        print() 
        print("Se han cargado exitosamente")
    elif opcion==2:
        bublist(apellido,nombre)
        print("Se han cargado exitosamente")


opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=int(input("Seleccione una opción (1-0): "))
    buttons(opcion)
    input("Presione Inter para continuar: ")
"""
#4)

cant=9
array=[1,2,3,4,5,6,7,8,9,0,0,0,0,cant]

def display_Array(array,cant):
    for x in range(cant):
        print(array[x],end=" ")
    print()

def a(array,entero):
    numero=int(input("¿Que número desea agregar al vector?: "))
    if (numero>=array[entero-1] and numero<=array[entero+1]) or (entero==0 and numero<=array[entero+1]):
        array[entero]=numero
        if entero>=array[-1]:
            array[-1]=entero+1
        for x in range(array[-1]):
            print(array[x],end=" ")
        print()
        print("Se han cargado exitosamente")
    else:
        print("ERROR! El número ingresado NO esta ordenado con el vector")


def b(array,entero):
    busqueda=False
    for x in range(array[-1]):
        if array[x]==entero:
            switch=array[x+1]
            array[x+1]=array[x]
            array[x]=switch
            busqueda=True

    if busqueda:
        array[-1]=array[-1]-1
        for x in range(array[-1]):
            print(array[x],end=" ")
        print()

    else:
        print("ERROR! El elemento que desea borrar NO se encuentra dentro del vector")


def insert(vector,entero):
    posicion=int(input("Posición: "))

    if entero>=vector[posicion-1] and entero<=vector[posicion+1]:
        posicion2=vector[-1]
        while posicion!=posicion2:
            switch=vector[posicion2]
            vector[posicion2]=vector[posicion2-1]
            vector[posicion2-1]=switch
            posicion2=posicion2-1
        
        vector[-1]=vector[-1]+1
        vector[posicion]=entero

        for x in range(vector[-1]):
            print(vector[x],end=" ")
        print()
    else:
        print("ERROR!")



def overdimension(array,accion,entero):
    if accion=="A":
        a(array,entero)
    elif accion=="B":
        b(array,entero)
    elif accion=="I":
        insert(array,entero)


def main_Menu():
    print("***MENU PRINCIPAL***")
    print()
    print("Seleccione la acción que desee realizar: ")
    print("1. Mostrar el vector ordenado.")
    print("A. Agregar un valor entero.")
    print("B. Borrar un valor entero.")
    print("I. Insertar un valor entero.")
    print("0. Salir.")
    print()

def buttons(opcion):
    if opcion=="1":
        display_Array(array,array[-1])
        print("Se han cargado exitosamente")  
    else:
        entero=int(input("Ingrese un valor entero: "))
        overdimension(array,opcion,entero)

opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=input("Seleccione una opción (1-0): ").upper()
    buttons(opcion)
    input("Presione Inter para continuar: ")


#----------------------------------------------------------------
#Ejercicios Adicionales

"""
#1)

vec1=[15,13,9,4,2]
vec2=[11,10,9,3,2]

def display_Array(array):
    for x in range(len(array)):
        print(array[x],end=" ")
    print()


def repeated_Array(vec1,vec2):
    vec3=[0]*len(vec1) or len(vec2)
    k=-1
    l=0
    for j in range(len(vec1) or len(vec2)):
        k=k+1
        for x in range(len(vec1) or len(vec2)):
            if vec1[k]==vec2[x]:
                vec3[l]=vec1[k]
                l=l+1

    return vec3


def main_Menu():
    print("***MENU PRINCIPAL***")
    print()
    print("1. Mostrar por pantalla los vectores.")
    print("2. Ordenar los números repetidos dentro de un vector terciario.")
    print("0. Salir.")
    print()

def buttons(opcion):
    if opcion==1:
        print()
        print("Vector #1")
        display_Array(vec1) 
        print()
        print("Vector #2")
        display_Array(vec2)  
        print()  
        print("Se han cargado exitosamente")
    elif opcion==2:
        vec3=repeated_Array(vec1,vec2)
        print("El vector",vec3,"se ha cargado exitosamente")


opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=int(input("Seleccione una opción (1-0): "))
    buttons(opcion)
    input("Presione Inter para continuar: ")

#2)


dockets=[0]*5
notes=[0]*(len(dockets)*3)


def load_Array(array,array2):
    for x in range(len(array)):
        array[x]=random.randint(14859,18493)
    for j in range(len(array2)):
        array2[j]=random.randint(1,10)


def display_Array(array,array2):
    posicion=0
    contador=0
    for x in range(len(array)):
        print("Legajo",array[x])
        print("Notas: ",end="")
        contador=0
        while contador<3:
            print(array2[posicion],end=" ")
            posicion=posicion+1
            contador=contador+1
        print()
        print()

def display_Array2(array,array2):
    for x in range(len(array)):
        print(array[x],array2[x])


def promedio(array,array2):
    posicion=-1
    contador=-1
    suma=[0]*len(array)
    for j in range(len(suma)):
        contador=contador+1
        for x in range(3):
            posicion=posicion+1
            suma[contador]=suma[contador]+array2[posicion]
        
    for x in range(len(suma)):
        suma[x]=suma[x]/3

    return suma



def main_Menu():
    print("***MENU PRINCIPAL***")
    print()
    print("1. Cargar la planilla completa.")
    print("2. Mostrar legajos y notas correspondientes.")
    print("3. Calcular el promedio de cada alumno y mostrar el listado.")
    print("0. Salir.")
    print()

def buttons(opcion):
    if opcion==1:
        load_Array(dockets,notes) 
        print("Se han cargado exitosamente")
    if opcion==2:
        os.system("cls")
        print("PLANILLA COMPLETA: ")
        display_Array(dockets,notes)   
        print("Se han cargado exitosamente")
    elif opcion==3:
        print("Legajos","Promedio")
        prmd=promedio(dockets,notes)
        display_Array2(dockets,prmd)
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