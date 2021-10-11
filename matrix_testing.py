


import numpy as np

"""
# -------------------------------------
# Vector en forma de lista (Heterogeneo)

vector=[0]*9 #Cantidad de elementos=9


# -------------------------------------
# Vector con NumPy (Homogeneo)

vector=np.array([0]*9)


#-------------------------------------
#Matriz con NumPy (Vector o Matriz de Dos Dimensiones)

#matrix=[[Valor Inicial]*Columnas]*Filas

#Con NumPy
#matrix=np.array([[Valor Inicial]*Columnas]*Filas)

matriz2d=np.array([[0]*9]*4)


#-------------------------------------
#Matriz 3D con NumPy (Matriz de Tres Dimensiones)

#matrix=[[[Valor Inicial]*Profundidad/Hoja/Dimensión]*Columnas]Filas

matriz3d=np.array([[[0]*2]*9]*3)



#--------------------------
#Mostrar el vector

def display_Array(vector):
    for x in range(len(vector)):
        print(vector[x],end=" ")

#display_Array(vector)

#--------------------------
#Mostrar la matriz

def display_Matray(matriz,filas,columnas):
    for f in range(filas):
        for c in range(columnas):
            print(matriz[f,c],end=" ")
        print()
    print()

#display_Matray(matriz2d,4,9)


#---------------------------
#Mostrar la matriz de Tres Dimensiones

#Para P desde 0 hasta Profundidad
    #Para F desde 0 hasta Filas
        #Para C desde 0 hasta Columnas
            #Mostrar (M[F,C,P])

def display_Matray3D(matriz,profundidad,filas,columnas):
    for p in range(profundidad):
        for f in range(filas):
            for c in range(columnas):
                print(matriz[f,c,p],end=" ")
            print()
        print()
    print()

display_Matray3D(matriz3d,2,3,9)


print("Tamaño: ",vector.size)
print()
print("Forma: ",vector.shape)
print()
print("Tamaño de la matriz: ",matriz2d.size)
print()
print("Tamaño de la matriz: ",matriz2d.shape)
print()
print("Tamaño de la matriz 3D: ",matriz3d.size)
print()
print("Forma de la matriz: ",matriz3d.shape)

array=[0]*5

matrix=[[9]*5]*2


columnas=3
filas=3


for x in range(len(matrix)):
    print(matrix[x])


#Crear una matriz inicializada en cero, con 2 columnas y 3 filas

matray=[[0]*2]*3

for x in range(len(matray)):
    print(matray[x])

#Crear una matriz inicializada en 2 y 5, y 3 y 4 con 2 columnas y 2 filas

matray2=[[[2,5],[3,4]]]*2

for x in range(len(matray2)):
    print(matray2[x])


atray=[]
for x in range(3):
    atray=atray+[[9]*2]

print(atray)

matrix=np.array(([0]*5) for x in range(5))

for x in range(1,10+1,2):
    print(x)

flotante=3.5
print(type(3.5))
"""

