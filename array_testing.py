



# variable=[0]*cant. de valores

"""
##numero=0 - Normal
##numero=[0]*50 - Vector
numero=[0]*50
posicion=0
while numero[posicion]!=-1:
    posicion=posicion+1
    numero[posicion]=int(input("Ingrese un número: "))
##print(numero,posicion) - Normal
##print(numero[4]) - Vector
print(numero[posicion])
"""

#vec1=[0]*5
#suma=0
#for x in range(5):
#    vec1[x]=int(input("Ing Nota: "))
#    suma=suma+vec1[x]
#
#print(vec1[3])

#for x in range(5):
#    print(vec1[x])  #Iteramos el contenido del vector

#for x in range(5):
#    print(x)  #Iteramos la posición del vector

#beck=[0]*5

#for x in range(5):
#    print(x)
#for x in range(1,5+1):
#    beck[x]=int(input("Text a number: "))
#    print(beck[2])

#whint=int(input("Cantidad: "))
#becket=[0]*(whint+1)
#for x in range(4):
#    becket[x]=int(input("Ingrese una nota: "))
#
"""
import random

array=[0]*250 #Se define al vector
arrayneg=[0]*250
arraysum=[0]*250
arraynone=[0]*250

def load_Array(array):
    for x in range(250): #Se itera un ciclo de 250 iteraciones
        array[x]=random.randint(-100,100) #random carga un número entre un rango específico

#Procesamiento del Vector       
def isnegatin(array,arrayneg,arraysum,arraynone):
    for x in range(250):
        if array[x]<0:
            arrayneg[x]==array[x]
        elif array[x]>0:
            arraysum[x]==array[x]
        elif array[x]==0:
            arraynone[x]==array[x]

def main_Menu():
    print("**MENU PRINCIPAL**")
    print()
    print("1. Mostrar por pantalla.")
    print("0. Salir.")

def buttons(opcion):
    if opcion==1:
        load_Array(array)
        isnegatin(array,arrayneg,arraysum,arraynone)
        print(array,arrayneg,arraysum,arraynone)
    
opcion=5
while opcion!=0:
    main_Menu()
    opcion=int(input("Seleccione una opción (0-1): "))
    buttons(opcion)

"""
"""
import random

vector=[0]*250
arraymajor=0

def show(vector):   #Se debe mostrar el vector siempre dentro de un ciclo, para que pueda tener asociado una posición
    print(vector)

#142 1
#143 2
#152 3     Indizado 
#72 4
#142 5
#942 6
#142 7


def major(vector,arraymajor):
    for x in range(250):
        vector[x]=random.randint(100,120)
        if vector[x]>arraymajor:
            arraymajor=vector[x]
    print(arraymajor)

major(vector,arraymajor)



import random

cantidad=0
cantidad2=0
cantidad3=0
array=[0]*250


def isnegatin(cantidad, cantidad2, cantidad3, array):
    for x in range(250):
        array[x]=random.randint(-100,100)
    if array[x]<0:
        cantidad=cantidad+1    
    elif array[x]>0:
        cantidad2=cantidad2+1
    elif array[x]==0:
        cantidad3=cantidad3+1
    return cantidad,cantidad2,cantidad3

#for x in range(250):
 #   cantidad, cantidad2, cantidad3 = x(cantidad, cantidad2, cantidad3, array)
  #  print("Hay" ,cantidad, "cantidad de números negativos")
   # print("Hay" ,cantidad2, "cantidad de números positivos")
    #print("Hay" ,cantidad3, "cantidad de números iguales a cero")
      

cantidad,cantidad2,cantidad3=isnegatin(array,cantidad,cantidad2,cantidad3)
print("Hay" ,cantidad, "cantidad de números negativos")
print("Hay" ,cantidad2, "cantidad de números positivos")
print("Hay" ,cantidad3, "cantidad de números iguales a cero")
"""
import numpy as np

"""
esta=False
while esta:
    print("!")


def crear_vector_long_n(n):
    array=[0 for x in range(n)]

array3=[[1,5,3,4,3,6,9],[2,3,5,7,9]]
print(array3)

for x in range(len(array3)):
    print(array3[x])
"""

"""
array=[9,3,6,1,5]
busqueda=int(input("¿Que número desea buscar?: "))

def busqueda_lineal(vector,target):
    posicion=-1
    contador=0
    while contador<len(vector) and posicion==-1:
        if vector[contador]==target:
            posicion=contador
        contador=contador+1

    return posicion

posicion=busqueda_lineal(array,busqueda)
print("Posicion",posicion)



for x in range(1):
    if array[x]>array[x+1]:
        switch=array[x]
        print(switch) 
        array[x]=array[x+1]
        print(switch) 
        array[x+1]=switch
        print(switch)
    
def busqueda_binaria_iter(vector, target):
    posicion=-1
    posicioni=0
    posicionf=len(vector)-1
    termino=False
    contador=0
    while posicioni<=posicionf and not(termino):
        medium=(posicioni+posicionf)//2
        if target==vector[medium]:
            termino=True
            posicion=medium

        elif target>vector[medium]:
            posicioni=medium+1

        elif target<vector[medium]:
            posicionf=medium-1

        contador=contador+1

    return contador,posicion


posicion=busqueda_binaria_iter(array,busqueda)
print("Esta en la posición",posicion)
"""
"""
arrayx=[0]*11
print(len(arrayx))

for x in range(11):
    print(x,end=" ")
print()



for x in range(11):
    elemento=elemento+1
    vector=[0]*elemento
    vector[0]=2
    print(vector,end=" ")

"""

cant=7
vector=[0,1,2,3,4,5,6,0,0,0,cant]

for x in range(cant):
    print(vector[x],end=" ")
print()

input()

def insert(vector):
    elemento=int(input("Elemento a ingresar: "))
    posicion=int(input("Posición: "))

    if elemento>=vector[posicion-1] and elemento<=vector[posicion+1]:
        posicion2=vector[-1]
        while posicion!=posicion2:
            switch=vector[posicion2]
            vector[posicion2]=vector[posicion2-1]
            vector[posicion2-1]=switch
            posicion2=posicion2-1
        
        vector[-1]=vector[-1]+1
        vector[posicion]=elemento

        for x in range(vector[-1]):
            print(vector[x],end=" ")
        print()
    else:
        print("ERROR!")

opcion=3
while 2+2==4:
    opcion=int(input("Enter: "))
    if opcion==1:
        insert(vector)

"""posicion 6 - 1 ciclos
posicion 6 - 1 ciclos
posicion 5 - 2 ciclos
posicion 4 - 3 ciclos
posicion 3 - 4 ciclos
posicion 2 - 5 ciclos
posicion 1 - 6 ciclos
posicion 0 - 7 ciclos
"""
