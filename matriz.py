#Código Ejemplo para utilizar Matrices Multidimensionales
# Este código se debe completar con:
#	 Cargar los arreglos con valores al azar (1, 2 y 3 dimensiones)
#	 Modificar las funciones para que solo reciban por parámetro el arreglo
#    Realizar una función que informe cuantos elementos pares, impares y ceros tiene cada arreglo

import numpy as np

def mostrarV(v):
    for i in range (len(v)):
        print(v[i],end=" ")
    print()

def mostrarM(m, filas,columnas):
    for f in range (filas):
        for c in range (columnas):
            print(m[f,c],end=" ")
        print()
    print()

def mostrar3(m, filas,columnas, profu):
    for p in range(profu):
        print("Profundidad:",p)
        for f in range (filas):
            for c in range (columnas):
                print(m[f,c,p],end=" ")
            print()
        print()
    print()


v0=[0]*10
v1=np.array([0]*10)
m2=np.array([[0]*10]*4)     #[0] valor a llenar, 10 columnas y 4 filas
m3=np.array([[[0]*2]*10]*4) #[0] valor a llenar, 10 columnas, 4 filas y 2 prof


mostrarV(v1)
input()
mostrarM(m2,4,10)
input()
print("3 dimensiones")
mostrar3(m3,4,10,2)
input()
print("vector",v1.size,v1.shape) 
print("Matriz",m2.size,m2.shape)
print("Tensor",m3.size,m3.shape)
