



#Trabajo Práctico 2

import random, os, numpy as np

#1)

matrix=np.array([[0]*4]*3)
matrix2=np.array([[0]*3]*3)

def load_Matray(matrix):
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    for f in range(filas):
        for c in range(columnas):
            matrix[f,c]=random.randint(-1,7)

def load_Matray2(matrix):
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    for f in range(filas):
        for c in range(columnas):
            matrix[f,c]=random.randint(1,50)

def load_Matray3(matrix):
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    for f in range(filas):
        for c in range(columnas):
            matrix[f,c]=random.randint(1,50)

def display_Matray(matrix):
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    for f in range(filas):
        for c in range(columnas):
            print(matrix[f,c],end=" ")
        print()
    print()


def sigma_Matrix(matrix):
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    suma=0
    for f in range(filas):
        for c in range(columnas):
            suma=suma+matrix[f,c]

    return suma


#2)
 
def sigma_Rows(matrix):
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    suma=np.array([0]*columnas)
    suma2=np.array([0]*filas)
    posicion=-1
    for f in range(filas): #3
        suma=suma+matrix[f]
        posicion=posicion+1
        for c in range(columnas): #3
            suma2[posicion]=suma2[posicion]+matrix[f,c]
    
    return suma,suma2


#3)


matrix3=np.array([[0]*3]*3)

load_Matray3(matrix3)
display_Matray(matrix3)

input()


switch=0
filas=matrix3.shape[0]
columnas=matrix3.shape[1]
fila=-1
for f in range(1):
    fila=fila+1
    for c in range(3):
        if f!=c:
            matrix3[f,c]=matrix3[f,c]+matrix3[f+1,fila]
            matrix3[f+1,fila]=matrix3[f,c]-matrix3[f+1,fila]
            matrix3[f,c]=matrix3[f,c]-matrix3[f+1,fila]



input()

display_Matray(matrix3)









"""



def main_Menu():
    print("***MENU PRINCIPAL***")
    print()
    print("1. Cargar la matriz.")
    print("2. Mostrar por pantalla la matriz.")
    print("3. Sumar todos los números de la matriz.")
    print("4. >>>SIGUIENTE>>.")
    print("0. Salir.")
    print()
    

def snd_Menu():
    print(">>>SIGUIENTE>>")
    print()
    print("1. Cargar números.")
    print("2. Mostrar por pantalla.")
    print("3. Calcular la suma de los números por filas y por columnas.")
    print("4. >>>SIGUIENTE>>.")
    print("0. Volver al menú principal.")
    print()


def trd_Menu():
    print(">>>SIGUIENTE>>")
    print()
    print("1. Cargar números.")
    print("2. Mostrar por pantalla.")
    print("3. Hacer la transpuesta de la matriz.")
    print("0. Volver al menú principal.")
    print()


def buttons2(opcion):
    if opcion==1:
        load_Matray(matrix2)  
        print("Se han cargado exitosamente")
    elif opcion==2:
        display_Matray(matrix2)   
        print()
        print("Se han cargado exitosamente")
    elif opcion==3:
        sigma1,sigma2=sigma_Rows(matrix2)
        print("La suma de los números en las filas es de: ",sigma2)
        print("La suma de los números en las columnas es de: ",sigma1)
    elif opcion==4:
        opcion3=5
        while opcion3!=0:
            os.system("cls")
            trd_Menu()
            opcion3=int(input("Seleccione una opción (1-3): "))
            buttons3(opcion3)
            input("Presione Inter para continuar: ")


def buttons3(opcion):
    if opcion==1:
        load_Matray3(matrix3)  
        print("Se han cargado exitosamente")
    elif opcion==2:
        display_Matray(matrix3)   
        print()
        print("Se han cargado exitosamente")
    elif opcion==3:
        3


def buttons(opcion):
    if opcion==1:
        load_Matray(matrix)
        print("Se han cargado exitosamente")
    elif opcion==2:
        display_Matray(matrix)
        print("Se han cargado exitosamente")
    elif opcion==3:
        suma=sigma_Matrix(matrix)
        print("La suma de todos los elementos de la matriz es de: ",suma)
    elif opcion==4:
        opcion2=5
        while opcion2!=0:
            os.system("cls")
            snd_Menu()
            opcion2=int(input("Seleccione una opción (1-3): "))
            buttons2(opcion2)
            input("Presione Inter para continuar: ")

    

opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=int(input("Seleccione una opción (1-3): "))
    buttons(opcion)
    input("Presione Inter para continuar: ")

"""