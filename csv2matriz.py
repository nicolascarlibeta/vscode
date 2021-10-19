#Cargar archivo csv a matriz
import pandas as pd 
import numpy as np
#Nos posicionamos en la carpeta donde esta el archivo desde la terminal
#Nombre del archivo de texto
#archi='/home/gcroch/Documentos/Program1/2021/matrices/datos.csv'
archi='datos.csv'

# Cargamos los datos del archivo usando la libreria panda 
datos=pd.read_csv(archi, sep=',',header=None)

#Mostramos las dimensiones de la estructura datos
print("Datos ",datos.shape[0],datos.shape[1])
input()

#Creamos la Matriz
mat=np.array([[" "*30]*datos.shape[1]]*datos.shape[0])
#Mostramos las dimensiones de la Matriz
print("Matriz ",mat.shape[0],mat.shape[1])

input("Comienza la carga de la matriz")
for i in range(datos.shape[0]):
    for j in range(datos.shape[1]):
        mat[i,j]=datos[j][i]

input("Ahora se muestra")
for i in range(datos.shape[0]):
    for j in range(datos.shape[1]):
#        print(mat[i,j],end=" ")
        print(f'{mat[i,j]:20}',end=" ")
    print(f'{mat[i,j]:20}',end=" ")
    print()

input("Ahora se muestra con nro de linea")
for i in range(datos.shape[0]):
    print(f'{i:5} {mat[i,0]:8} {mat[i,1]:25} {mat[i,2]:25} {mat[i,3]:10}')
print()
print("Ahora pueden usar la matriz para realizar búsquedas...")