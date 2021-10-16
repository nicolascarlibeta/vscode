

import numpy as np, random, os

#Ordenamiento de Matrices:

#Ordenamiento completo

#Se debera crear un vector terciario que acumule los valores de la matriz
"""
matrix=np.array([[5,1,6,2,4],[3,5,5,2,19]])
tamaño=matrix.size
vector=np.array([0]*tamaño)

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
"""

matrix2=np.array([[1,1,6,2,4],[2,5,5,2,19],[2,4,5,6,9],[5,6,3,5,5]])
    

filas=matrix2.shape[0]
columnas=matrix2.shape[1]
for f in range(filas):
    for c in range(columnas):
        print(matrix2[f,c],end=" ")
    print()
print() 


input()


filas=matrix2.shape[0]
columnas=matrix2.shape[1]
switch=np.array([0]*columnas)
for f in range(filas-1):
    for c in range(columnas):
        if matrix2[f,3]>matrix2[f+1,3]:
            print("!",end=" ")


for c in range(columnas):    
    switch[c]=matrix2[2,c]

for c in range(columnas):
    matrix2[2,c]=matrix2[2+1,c]

for c in range(columnas):
    matrix2[2+1,c]=switch[c]
            
input()

for f in range(filas):
    for c in range(columnas):
        print(matrix2[f,c],end=" ")
    print()
print()












"""
def main_Menu():
    print("***MENU PRINCIPAL***")
    print()
    print("1. Mostrar por pantalla la matriz.")
    print("2. Ordenar completamente la matriz.")
    print("0. Salir.")
    print()

    
def buttons(opcion):
    if opcion==1:
        display_Matray(matrix) 
        print("Se han cargado exitosamente")
    elif opcion==2:
        complete_Ordering(matrix)   
        print("Se ha ordenado exitosamente")


opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=int(input("Seleccione una opción (1-3): "))
    buttons(opcion)
    input("Presione Inter para continuar: ")
"""


