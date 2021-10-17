

import numpy as np, random, os

#Ordenamiento de Matrices:

#Ordenamiento completo

#Se debera crear un vector terciario que acumule los valores de la matriz

matrix=np.array([[5,1,6,2,4],[3,5,5,2,19]])
tamaño=matrix.size
vector=np.array([0]*tamaño)
"""
filas=matrix.shape[0]
columnas=matrix.shape[1]
for f in range(filas):
    for c in range(columnas):
        print(matrix[f,c],end=" ")
    print()
print()

input()


posicion=0
for f in range(filas):
    for c in range(columnas): #0,5
        vector[posicion]=matrix[f,c]
        posicion=posicion+1
            
input()

for x in range(len(vector)):
    print(vector[x],end=" ")
print()


#Una vez que esten acumulados, ordenamos los números dentro del vector

termino=False
lenght=len(vector)
while not(termino):
    lenght=lenght-1
    termino=True
    for x in range(lenght):
        if vector[x]>vector[x+1]:
            switch=vector[x]
            vector[x]=vector[x+1]
            vector[x+1]=switch
            termino=False


input()

for x in range(len(vector)):
    print(vector[x],end=" ")

input()

#Por último, revertimos el primer paso


posicion=0
for f in range(filas):
    for c in range(columnas): #0,5
        matrix[f,c]=vector[posicion]
        posicion=posicion+1

input()

for f in range(filas):
    for c in range(columnas):
        print(matrix[f,c],end=" ")
    print()
print()
"""

matrix=np.array([[5,1,6,2,4],[3,5,5,2,19]])
tamaño=matrix.size
vector=np.array([0]*tamaño)


def display_Matray(matrix):
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    for f in range(filas):
        for c in range(columnas):
            print(matrix[f,c],end=" ")
        print()
    print() 


def complete_Ordering(matrix):
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    posicion=0
    for f in range(filas):
        for c in range(columnas): #0,5
            vector[posicion]=matrix[f,c]
            posicion=posicion+1
    
    termino=False
    lenght=len(vector)
    while not(termino):
        lenght=lenght-1
        termino=True
        for x in range(lenght):
            if vector[x]>vector[x+1]:
                switch=vector[x]
                vector[x]=vector[x+1]
                vector[x+1]=switch
                termino=False
    
    posicion=0
    for f in range(filas):
        for c in range(columnas): #0,5
            matrix[f,c]=vector[posicion]
            posicion=posicion+1


#Ordenamiento por columna

#Ordenamos la columna
#Si existe un valor mayor ante un valor menor, la fila se invierte
#Asi, hasta que quede la columna ordenada


matrix2=np.array([[4,6,7,4,2],[8,3,6,9,11],[2,1,5,14,9],[5,0,3,12,5]])


def switch_Matray(matrix,f,columna):
    columnas=matrix.shape[1]
    switch=np.array([0]*columnas)
    if matrix2[f,columna]>matrix2[f+1,columna]:
        for j in range(columnas):
            switch[j]=matrix[f,j]
            matrix[f,j]=matrix[f+1,j]
            matrix[f+1,j]=switch[j]


def column_Ordering(matrix,columna):
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    for x in range(filas-1):
        for f in range(filas-1):
            for c in range(columnas):
                switch_Matray(matrix,f,columna)
            
            

#Ordenamiento por índice

#Creamos un vector con la misma cantidad de filas
#Buscamos de menor a mayor en la fila, y anotamos su posición
#Agregamos las posiciones en un vector del mismo tamaño de filas



matrix3=np.array([["Go With The Flow","2002"],["Anthem","2009"],["Higher Ground","1989"],["In Bloom","1991"],["I Can't Hear You","2006"]])
matrix4=np.array([["Go With The Flow","2002"],["Anthem","2009"],["Higher Ground","1989"],["In Bloom","1991"],["I Can't Hear You","2006"]])


    
def indexing_Ord(matrix,columna):
    fila=0
    row=0
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    menor=matrix[0,columna]
    for f in range(filas):
        for c in range(columnas):
            if matrix[f,columna]<menor:
                menor=matrix[f,columna]
                fila=f
                row=c

    return fila,row

def index_Ordering(matrix,columna):
    filas=matrix.shape[0]
    for x in range(filas):
        fila,row=indexing_Ord(matrix,columna)
        vector[x]=fila
        matrix[fila,row]="zzzzz"


filas=matrix3.shape[0]
columnas=matrix3.shape[1]
for j in range(len(vector)):
    print(matrix3[vector[j],vector[j]])


input()






def main_Menu():
    print("***MENU PRINCIPAL***")
    print()
    print("1. Mostrar por pantalla la matriz.")
    print("2. Ordenar completamente la matriz.")
    print("3. Ordenar por columna.")
    print("0. Salir.")
    print()

    
def buttons(opcion):
    if opcion==1:
        print("Matriz #1")
        display_Matray(matrix)
        print("Matriz #2") 
        display_Matray(matrix2) 
        print("Se han cargado exitosamente")
    elif opcion==2:
        complete_Ordering(matrix)   
        print("Se ha ordenado exitosamente")
    elif opcion==3:
        columna=int(input("Por favor, ingrese la columna que desea ordenar: "))
        column_Ordering(matrix2,columna)
        print("Se ha ordenado exitosamente")
    elif opcion==4:
        columna=int(input("Por favor, ingrese la columna que desea ordenar: "))
        index_Ordering(matrix4,columna)
        print("Se ha ordenado exitosamente")


opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=int(input("Seleccione una opción (1-3): "))
    buttons(opcion)
    input("Presione Inter para continuar: ")



