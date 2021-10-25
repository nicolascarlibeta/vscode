

#Código Ejemplo para utilizar Matrices Multidimensionales
# Este código se debe completar con:
#	 Cargar los arreglos con valores al azar (1, 2 y 3 dimensiones)
#	 Modificar las funciones para que solo reciban por parámetro el arreglo
#    Realizar una función que informe cuantos elementos pares, impares y ceros tiene cada arreglo

import numpy as np, random, os

"""
numero=0
filas=5
columnas=9
array=np.array([(x*5) for x in range(1,9)])
matrix=np.array([[numero]*columnas]*filas)


#¿Como se recorre a un vector?

def display_Array(array):
    for x in range(len(array)):
        print(array[x],end=" ")
    print()

def load_Matray(matrix):
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    for f in range(filas):
        for c in range(columnas):
            matrix[f,c]=random.randint(3,9)

def load_Tensor(tensor):
    hoja=tensor.shape[2]
    filas=tensor.shape[0]
    columnas=tensor.shape[1]
    for h in range(hoja):
        for f in range(filas):
            for c in range(columnas):
                tensor[f,c,h]=random.randint(3,9)


def pair_Entry(matrix):
    impares=0
    pares=0
    ceros=0
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    for f in range(filas):
        for c in range(columnas):
            if (matrix[f,c]%2)==1:
                impares=impares+1

            elif (matrix[f,c]%2)==0:
                pares=pares+1

            if matrix[f,c]==0:
                ceros=ceros+1

    print("La cantidad de números pares es de:",pares)
    print("La cantidad de números impares es de:",impares)
    print("La cantidad de números iguales a cero es de:",ceros)


def pair_Tensor(tensor):
    impares=0
    pares=0
    ceros=0
    hoja=tensor.shape[2]
    filas=tensor.shape[0]
    columnas=tensor.shape[1]
    for h in range(hoja):
        for f in range(filas):
            for c in range(columnas):
                if (tensor[f,c,h]%2)==1:
                    impares=impares+1

                elif (tensor[f,c,h]%2)==0:
                    pares=pares+1

                if tensor[f,c,h]==0:
                    ceros=ceros+1

    print("La cantidad de números pares es de:",pares)
    print("La cantidad de números impares es de:",impares)
    print("La cantidad de números iguales a cero es de:",ceros)


def pair_Array(array):
    impares=0
    pares=0
    ceros=0
    for x in range(len(array)):
        if (array[x]%2)==1:
            impares=impares+1

        elif (array[x]%2)==0:
            pares=pares+1

        if array[x]==0:
            ceros=ceros+1

    print("La cantidad de números pares es de:",pares)
    print("La cantidad de números impares es de:",impares)
    print("La cantidad de números iguales a cero es de:",ceros)

    
#¿Como se recorre a una matriz?

def display_Entry(matrix):
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    for j in range(filas):
        for x in range(columnas):
            print(matrix[j,x],end=" ")
        print()
    print()

tensor=np.array([[[numero]*2]*columnas]*filas)
hoja=2

#¿Como se recorre un tensor?

def display_Tensor(tensor):
    hoja=tensor.shape[2]
    filas=tensor.shape[0]
    columnas=tensor.shape[1]
    for h in range(hoja):   
        print("Hoja",h)
        for f in range(filas):
            for c in range(columnas):
                print(tensor[f,c,h],end=" ")
            print()
        print()

#print(vector.size,vector.shape)
#print(tensor.size,tensor.shape)


display_Array(array)
input()
pair_Array(array)
input()
load_Matray(matrix)
display_Entry(matrix)
input()
pair_Entry(matrix)
input()
load_Tensor(tensor)
display_Tensor(tensor)
input()
pair_Tensor(tensor)
"""

#1)
""" """
matrix=np.array([[0]*10]*10)

def load_Matray(matrix):
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    for f in range(filas):
        for c in range(columnas):
            matrix[f,c]=random.randint(1,500)

def display_Matray(matrix):
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    for f in range(filas):
        for c in range(columnas):
            print(matrix[f,c],end=" ")
        print()
    print() 

#a)
def unpair_Summary(matrix):
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    suma=0
    for f in range(1,filas+1,2):
        for c in range(columnas):
            if (matrix[f,c]%2)==0:
                suma=suma+matrix[f,c]   

                
    return suma

#b)
def five_Multiple(matrix):
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    contador=0
    for f in range(filas):
        for c in range(columnas):
            if (matrix[f,c]%5)==0:
                contador=contador+1

    return contador

#c)
def tfe_Multiples(matrix):
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    three=False
    five=False
    eleven=False
    for f in range(filas):
        for c in range(columnas):
            if (matrix[f,c]%3)==0:
                three=True
            
            elif (matrix[f,c]%5)==0:
                five=True

            elif (matrix[f,c]%11)==0:
                eleven=True
    
    return three,five,eleven

#d)
def prime_Id(matrix,f,c):
    termino=False
    contador=2
    if matrix[f,c]<2:
        termino=True
    while contador<matrix[f,c] and not(termino):
        if (matrix[f,c]%contador)==0:
            termino=True
        contador=contador+1

    return termino

def prime_Numbers(matrix):
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    for f in range(filas):
        for c in range(columnas):
            if prime_Id(matrix,f,c)==False:
                    print(matrix[f,c],end=". ")
    
#e)
def menor_columna(matrix,columna):
    filas=matrix.shape[0]
    menor=matrix[0,columna]
    steps=1
    fila=0
    for f in range(steps):
        for x in range(filas): #5
            if matrix[x,columna]<menor:
                menor=matrix[x,columna]
                fila=x

    return matrix,menor,fila


def mayor_fila(matrix,menor,fila):
    columnas=matrix.shape[1]
    termino=False
    contador=0
    while contador<columnas and not(termino):
        if menor<matrix[fila,contador]:
            termino=True
        contador=contador+1

    
    return termino


def saddle_Point(matrix):      
    filas=matrix.shape[0]
    columna=-1
    termino=False
    contador=0
    while contador<filas and not(termino):
        columna=columna+1
        matrix,minor,rows=menor_columna(matrix,columna)
        sp=mayor_fila(matrix,minor,rows)
        if sp==False:
            print("La matriz actual SI posee punto de silla, y es el número",minor)
            termino=True
        contador=contador+1

    if sp==True:
        print("La matriz actual NO posee punto de silla.")


def main_Menu():
    print("***MENU PRINCIPAL***")
    print()
    print("1. Cargar la matriz.")
    print("2. Mostrar por pantalla la matriz.")
    print("3. Sumar los números pares en las filas impares.")
    print("4. Calcular la cantidad de números multiplos de 5.")
    print("5. Informar si existe al menos un número múltiplo de 3, 5 y 11.")
    print("6. Mostrar todos los números primos dentro de la matriz.")
    print("7. Informar si la matríz posee punto de silla.")
    print("0. Salir.")
    print()

def buttons(opcion):
    if opcion==1:
        load_Matray(matrix)  
        print("Se han cargado exitosamente")
    elif opcion==2:
        print()
        display_Matray(matrix)   
        print()
        print("Se han cargado exitosamente")
    elif opcion==3:
        suma=unpair_Summary(matrix)
        print("La suma de los números pares en las filas impares es de: ",suma)
        print()
    elif opcion==4:
        multiplos=five_Multiple(matrix)
        print("La cantidad de números multiplos de 5 es de: ",multiplos)
    elif opcion==5:
        tres,cinco,once=tfe_Multiples(matrix)
        if tres:
            print("Existe al menos un número múltiplo de 3")
        else:
            print("No existe ningún número múltiplo de 3")
        if cinco:
            print("Existe al menos un número múltiplo de 5")
        else:
            print("No existe ningún número múltiplo de 5")
        if once:
            print("Existe al menos un número múltiplo de 11")
        else:
            print("No existe ningún número múltiplo de 11")
    elif opcion==6:
        print("Los números primos que se encuentran dentro de la matriz son: ")
        prime_Numbers(matrix)
        print()
    elif opcion==7:
        saddle_Point(matrix)


opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=int(input("Seleccione una opción (1-3): "))
    buttons(opcion)
    input("Presione Inter para continuar: ")


#2)

matrix=np.array([[0]*3]*3)


def load_Matray(matrix):
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    for f in range(filas):
        for c in range(columnas):
            matrix[f,c]=random.randint(0,5)


def display_Matray(matrix):
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    for f in range(filas):
        for c in range(columnas):
            print(matrix[f,c],end=" ")
        print()
    print() 

#a)
def interchange(matrix,f,c):
    switch=np.array([0])
    switch[0]=switch[0]+matrix[f,c]
    matrix[f,c]=matrix[c,f]
    matrix[c,f]=switch[0]

def trainspotting(matrix):
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    columna=0
    for f in range(filas):
        columna=columna+1
        for c in range(columna,columnas):
            interchange(matrix,f,c)
            


def main_Menu():
    print("***MENU PRINCIPAL***")
    print()
    print("1. Cargar la matriz de 3x3.")
    print("2. Mostrar por pantalla la matriz.")
    print("3. Realizar la transpuesta de la matriz.")
    print("0. Salir.")
    print()

    
def buttons(opcion):
    if opcion==1:
        load_Matray(matrix)  
        print("Se han cargado exitosamente")
    elif opcion==2:
        print()
        display_Matray(matrix)   
        print()
        print("Se han cargado exitosamente")
    elif opcion==3:
        trainspotting(matrix)   
        print("Se han cargado exitosamente")


opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=int(input("Seleccione una opción (1-3): "))
    buttons(opcion)
    input("Presione Inter para continuar: ")