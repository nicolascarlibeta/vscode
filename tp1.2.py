



import os
#Trabajo Práctico 1.2
import random

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
"""

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

array=[2,4,6,9]
array2=[3,7,9,11,13,15]
tamaño=len(array+array2)
array3=[0]*tamaño

def display_Array(array):
    for x in range(len(array)):
        print(array[x], end=" ")


def ordering(array,array2):
    x=0
    j=0
    k=0
    while x<len(array) and j<len(array2):
        if array[x]==array2[j]:
            array3[k]=array[x]

        elif array[x]<array2[j]:
            array3[k]=array[x]
            x=x+1
            j=j+1
            k=k+1
        else:
            array3[k]=array2[j]
            j=j+1
            k=k+1
            
    return array3



        


def main_Menu():
    print("***MENU PRINCIPAL***")
    print()
    print("1. Mostrar por pantalla los vectores.")
    print("2. Ordenar dentro de un vector secundario.")
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


#4)
"""
array=[1,2,3,4,5,6,7,8,9,0,0]
cantidad_util=9

for x in range(cantidad_util):
    print(array[x],end=" ")
print()

def overdimension(array,opcion,entero):
    cantidad_util=9
    if opcion=="a":
        numero=int(input("¿Que número desea agregar al vector?: "))
        array[entero]=numero   
        if entero>=cantidad_util:
            cantidad_util=entero+1
            if cantidad_util>len(array):
               print("ERROR! Se excedio el límite: No se pueden agregar mas elementos")
        
        for x in range(cantidad_util):
            print(array[x],end=" ")

    elif opcion=="b":
        for x in range(cantidad_util):
            if array[x]==entero:
                switch=array[x+1]
                array[x+1]=array[x]
                array[x]=switch

        cantidad_util=cantidad_util-1
        for x in range(cantidad_util):
            print(array[x],end=" ")

    elif opcion=="i":
        posicion=int(input("¿En que posición desea insertar el elemento?: "))
        ciclos=cantidad_util-posicion
        posicion2=cantidad_util
        for x in range(ciclos):
            switch=array[posicion2]
            array[posicion2]=array[posicion2-1]
            array[posicion2-1]=switch
            posicion2=posicion2-1

        cantidad_util=cantidad_util+1
        array[posicion]=entero
        for x in range(cantidad_util):
            print(array[x],end=" ")


input()
overdimension(array,"b",3)

"""
