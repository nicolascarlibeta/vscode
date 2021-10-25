



#Trabajo Práctico 2

import random, os, numpy as np

#1)
"""
matrix=np.array([[0]*4]*3)
matrix2=np.array([[0]*3]*3)
matrix3=np.array([[0]*3]*3)

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

def permutation(matrix):
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    for f in range(filas-1):
        for c in range(columnas):
            if f!=c and f!=1:
                matrix[f,c]=matrix[f,c]+matrix[c,f]
                matrix[c,f]=matrix[f,c]-matrix[c,f]
                matrix[f,c]=matrix[f,c]-matrix[c,f]
            elif c==2:
                matrix[f,c]=matrix[f,c]+matrix[c,f]
                matrix[c,f]=matrix[f,c]-matrix[c,f]
                matrix[f,c]=matrix[f,c]-matrix[c,f]

    return matrix




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
        permutation(matrix3)
        print("Se han cargado exitosamente")


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

#----------------------------------------------------------------
#Ejercicios Adicionales


#1)

"""
matrix=np.array([[0]*10]*3)

def load_Matray(matrix):
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    for f in range(filas):
        for c in range(columnas):
            matrix[f,c]=random.randint(19,34)

def display_Matray(matrix):
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    for f in range(filas):
        for c in range(columnas):
            print(matrix[f,c],end=" ")
        print()
    print()


def promedio(matrix):
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    suma=0
    for f in range(filas):
        for c in range(columnas):
            suma=suma+matrix[f,c]

    return suma


def maxymin_temperatura(matrix):
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    mayor=matrix[0,0]
    menor=matrix[0,0]
    contador=0
    contador2=0
    dia=0
    dia2=0
    for f in range(filas):
        for c in range(columnas):
            if matrix[f,c]>mayor:
                mayor=matrix[f,c]
                dia=contador
            elif matrix[f,c]<menor:
                menor=matrix[f,c]
                dia2=contador2

            contador=contador+1
            contador2=contador2+1
    return mayor,dia,menor,dia2




def main_Menu():
    print("***MENU PRINCIPAL***")
    print()
    print("1. Cargar las temperaturas minimas y máximas del mes.")
    print("2. Mostrar el calendario.")
    print("3. Calcular el promedio total de temperaturas.")
    print("4. Informar el dia de máxima y minima temperatura.")
    print("0. Salir.")
    print()

def buttons(opcion):
    if opcion==1:
        load_Matray(matrix)  
        print("Se han cargado exitosamente")
    elif opcion==2:
        display_Matray(matrix)   
        print()
        print("Se han cargado exitosamente")
    elif opcion==3:
        suma=promedio(matrix)
        prmd=suma/matrix.size
        print("El promedio de temperaturas total del mes es de:",prmd)
    elif opcion==4:
        mayor,dia,menor,dia2=maxymin_temperatura(matrix)
        print("El dia de máxima temperatura fue el",dia,"con una temperatura de",mayor,"grados")
        print("El dia de minima temperatura fue el",dia2,"con una temperatura de",menor,"grados")

        
    

opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=int(input("Seleccione una opción (1-3): "))
    buttons(opcion)
    input("Presione Inter para continuar: ")


#2)

matrix=np.array([["abcdefgh"]*3]*20)


def load_Matray(matrix):
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    for f in range(filas):
        for c in range(1):
            nombre=input("Por favor, ingrese un nombre: ")
            apellido=input("Por favor, ingrese un apellido: ")
            documento=input("Por favor, ingrese un D.N.I.: ")
            matrix[f,c]=nombre
            matrix[f,c+1]=apellido
            matrix[f,c+2]=documento


def display_Matray(matrix):
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    for f in range(filas):
        for c in range(columnas):
            print(matrix[f,c],end=" ")
        print()
    print()


def colsort_stepone(matrix,f,c):
    columnas=matrix.shape[1]
    switch=[0]*columnas
    if matrix[f,c]>matrix[f+1,c]:
        for x in range(columnas):
            switch[x]=matrix[f,x]
            matrix[f,x]=matrix[f+1,x]
            matrix[f+1,x]=switch[x]


def colsort_steptwo(matrix,columna):
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    for f in range(filas-1):
        for c in range(columnas):
            colsort_stepone(matrix,f,columna)


def colsort(matrix,columna):           
    filas=matrix.shape[0]
    for x in range(filas-1):
        colsort_steptwo(matrix,columna)




def main_Menu():
    print("***MENU PRINCIPAL***")
    print()
    print("1. Cargar los datos personales.")
    print("2. Mostrar los datos completos.")
    print("3. Ordenar por: Apellido (A-Z).")
    print("0. Salir.")
    print()

def buttons(opcion):
    if opcion==1:
        load_Matray(matrix)  
        print("Se han cargado exitosamente")
    if opcion==2:
        display_Matray(matrix)  
        print("Se han cargado exitosamente")
    elif opcion==3:
        apellido=1
        colsort(matrix,apellido)
        
    

opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=int(input("Seleccione una opción (1-3): "))
    buttons(opcion)
    input("Presione Inter para continuar: ")

"""
#3)

matrix=np.array([[[0]*3]*20]*4)

def load_Tensor(matrix):
    hoja=matrix.shape[2]
    filas=matrix.shape[0]
    columnas=matrix.shape[1]    
    for h in range(hoja):
        for f in range(filas):
            for c in range(columnas):
                matrix[f,c,h]=random.randint(1,10)
                

def display_Tensor(matrix):
    hoja=matrix.shape[2]
    filas=matrix.shape[0]
    columnas=matrix.shape[1]    
    for h in range(hoja):
        print("Universidad",h+100)
        for f in range(filas):
            for c in range(columnas):
                print(matrix[f,c,h],end=" ")
            print()
        print()
    print()



def promedioxCurso(matrix):
    hoja=matrix.shape[2]
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    contador=-1
    suma=[0]*filas
    cantidad=hoja*columnas
    for f in range(filas):
        contador=contador+1
        for h in range(hoja):
            for c in range(columnas):
                suma[contador]=suma[contador]+matrix[f,c,h]
    
    
    for x in range(len(suma)):
        suma[x]=suma[x]/cantidad
    
    return suma

  
def promedioxCentro(matrix):
    hoja=matrix.shape[2]
    filas=matrix.shape[0]
    columnas=matrix.shape[1]    
    posicion=-1
    suma=[0]*hoja
    cantidad=filas*columnas
    for h in range(hoja):
        posicion=posicion+1
        for f in range(filas):
            for c in range(columnas):
                    suma[posicion]=suma[posicion]+matrix[f,c,h]
            
    for x in range(len(suma)):
        suma[x]=suma[x]/cantidad
    
    return suma


def sigma_Tensor(matrix):
    hoja=matrix.shape[2]
    filas=matrix.shape[0]
    columnas=matrix.shape[1]
    cantidad=filas*columnas*hoja 
    suma=0    
    for h in range(hoja):
        for f in range(filas):
            for c in range(columnas):
                suma=suma+matrix[f,c,h]

    promedio=suma/cantidad
    return promedio
    

def curso(matrix,hj):
    hoja=matrix.shape[2]
    filas=matrix.shape[0]
    columnas=matrix.shape[1]   
    for h in range(1):
        for f in range(filas):
            for c in range(columnas):
                print(matrix[f,c,hj],end=" ")
            print()
        print()
    print()


def bubsort(array): 
    termino=False
    lenght=len(array)
    while not(termino):
        lenght=lenght-1
        termino=True
        for x in range(lenght):
            if array[x+1]>array[x]:
                switch=array[x+1]
                array[x+1]=array[x]
                array[x]=switch
                termino=False


def mayor_centro(matrix,array):
    vector=np.array([array[0],array[1],array[2]])
    bubsort(vector) #Ordenar el vector#----------------
    #Posición 1#--------------------------
    if vector[0]==array[0]:
        print("Universidad 100")
        curso(matrix,0)
    elif vector[0]==array[1]:
        print("Universidad 101")
        curso(matrix,1)
    elif vector[0]==array[2]:
        print("Universidad 102")
        curso(matrix,2)
    #Posición 2#--------------------------
    if vector[1]==array[0]:
        print("Universidad 100")
        curso(matrix,0)
    elif vector[1]==array[1]:
        print("Universidad 101")
        curso(matrix,1)
    elif vector[1]==array[2]:
        print("Universidad 102")
        curso(matrix,2)
    


def main_Menu():
    print("***MENU PRINCIPAL***")
    print()
    print("1. Cargar la planilla.")
    print("2. Mostrar los datos completos.")
    print("3. Calcular la nota promedio por curso.")
    print("4. Calcular la nota promedio por centro.")
    print("5. Calcular la nota promedio en general.")
    print("6. Mostar los dos mejores centros y sus respectivas notas.")
    print("0. Salir.")
    print()

def buttons(opcion):
    if opcion==1:
        load_Tensor(matrix)  
        print("Se han cargado exitosamente")
    if opcion==2:
        display_Tensor(matrix)   
        print("Se han cargado exitosamente")
    if opcion==3:
        promedio=promedioxCurso(matrix)
        print("La nota promedio del 1er curso es de: ",promedio[0])
        print("La nota promedio del 2do curso es de: ",promedio[1])
        print("La nota promedio del 3er curso es de: ",promedio[2])
        print("La nota promedio del 4to curso es de: ",promedio[3])
    if opcion==4:
        promedioc=promedioxCentro(matrix)
        print("La nota promedio de la universidad 100 es de: ",promedioc[0])
        print("La nota promedio de la universidad 101 es de: ",promedioc[1])
        print("La nota promedio de la universidad 102 es de: ",promedioc[2])
    if opcion==5:
        promediot=sigma_Tensor(matrix)
        print("La nota promedio en general es de: ",promediot)
    if opcion==6:
        promedioc=promedioxCentro(matrix)
        print("Los dos centros con la mejor calificación son: ")
        print()
        mayor_centro(matrix,promedioc)

opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=int(input("Seleccione una opción (1-3): "))
    buttons(opcion)
    input("Presione Inter para continuar: ")