-"""

#Trabajo Práctico 1

import random, os

#1)

#Un vector es como un cubo con una cierta capacidad de objetos que se pueden meter

array=[0]*250 #Se define al vector
arraymajor=0

#Carga del Vector
def load_Array(array):
    for x in range(250): #Se itera un ciclo de 250 iteraciones
        array[x]=random.randint(-100,100) #random carga un número entre un rango específico

#Muestra por pantalla del vector
def display_Array(array):
    for x in range(250):
        print(array[x], end=" ")
        
#Procesamiento del Vector       
def isnegatin(array):
    cantidad=0
    cantidad2=0
    cantidad3=0
    for x in range(250):
        if array[x]<0:
            cantidad=cantidad+1
        elif array[x]>0:
            cantidad2=cantidad2+1
        elif array[x]==0:
            cantidad3=cantidad3+1
    return cantidad,cantidad2,cantidad3

#Calculo del número mayor dentro del vector
def major_Number(arraymajor):
    for x in range(250):
        if array[x]>arraymajor:
            arraymajor=array[x]
    return arraymajor

#Calculo de suma de números en posiciones impares
def unpair_Numbers(array):
    suma=0
    for x in range(250):
        if (x%2)==1:
            array[x]
            suma=suma+array[x]
    print("La suma de los números en las posiciones impares es: ",suma)

def main_Menu():
    print(" "*39,"★★★ MENÚ PRINCIPAL★★★")
    print()
    print(" "*25,"1. Cargar 250 números aleatorios entre -100 y 100.")
    print(" "*25,"2. Mostrar por pantalla los números contenidos.")
    print(" "*25,"3. Calcular la cantidad de números negativos, positivos y ceros.")
    print(" "*25,"4. Encontrar al número mas grande de todos.")
    print(" "*25,"5. Sumar los números con posiciones impares.")
    print(" "*25,"0. Salir.")
    print()

def buttons(opcion):
    if opcion==1:
        load_Array(array)  #Carga los números
        print("Se han cargado exitosamente")
    elif opcion==2:
        display_Array(array)   #Muestra los números por pantalla
        print()
        print("Se han cargado exitosamente")
    elif opcion==3:
        cantidad,cantidad2,cantidad3=isnegatin(array)
        print("Hay" ,cantidad, "cantidad de números negativos")
        print("Hay" ,cantidad2, "cantidad de números positivos")
        print("Hay" ,cantidad3, "cantidad de números iguales a cero")
    elif opcion==4:
        print("El número mas grande entre todos es el",major_Number(arraymajor))  #Muestra el número mas grande por pantalla
    elif opcion==5:
        unpair_Numbers(array)  #Muestra la suma de los números con posiciones impares

opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=int(input("Seleccione una opción (1-5): "))
    buttons(opcion)
    input("Presione Inter para continuar: ")



#2)

array=[0]*10

def load_Array(array):
   for x in range(10):
       array[x]=input("Hola, por favor ingrese su apellido: ")

def display_Array(array):
    for x in range(10):
        print(array[x], end=" ")

def surname():
    apellido=input("Buscar...: ")
    return apellido

def search_IfSur(array,apellido):
    for x in range(10):
        if array[x]==apellido:
            return True

#Otra forma de realizarlo
def search_IfSur(array,apellido):
    esta=False
    for x in range(10):
        if array[x]==apellido:
            esta=True
    return esta 

#Con un While
def search_IfSur(array,apellido):
    iteraciones=0
    this=False
    while iteraciones<10 and this==False:
        if array[iteraciones]==apellido:
            this=True
        iteraciones=iteraciones+1 #a partir de que termine el ciclo, la iteracion va a sumar 1, o sea la 1era posicion
    return this 

#Menú Principal
def main_Menu():
    print("***MENU PRINCIPAL***")
    print()
    print("1. Cargar los apellidos de 10 alumnos.")
    print("2. Mostrar por pantalla los apellidos contenidos.")
    print("3. Buscar por apellido...")
    print("0. Salir.")
    print()

def buttons(opcion):
    if opcion==1:
        load_Array(array)  #Carga los números
        print("Se han cargado exitosamente")
    elif opcion==2:
        display_Array(array)   #Muestra los números por pantalla
        print()
        print("Se han cargado exitosamente")
    elif opcion==3:
        apellido=surname()
        if search_IfSur(array,apellido)==True:
            print("El apellido se encuentra en la lista")
        else:
            print("No hay coincidencias en su busqueda")     

opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=int(input("Seleccione una opción (1-3): "))
    buttons(opcion)
    input("Presione Inter para continuar: ")



#3)

array=[0]*5000

def load_Array(array):
   for x in range(5000):
       array[x]=random.randint(18,80)

def display_Array(array):
    for x in range(5000):
        print(array[x],end=" ")

def frequency(array):
    freq=[0]*81
    mayor=0
    for x in range(5000):
        posicion=array[x]
        freq[posicion]=freq[posicion]+1
        if freq[posicion]>mayor:
            mayor=freq[posicion]
            edad=posicion
    print("La edad que más se repite es",edad,"y se repite una cantidad de",mayor,"veces")


#Menú Principal
def main_Menu():
    print("***MENU PRINCIPAL***")
    print()
    print("1. Cargar 5000 edades")
    print("2. Mostrar por pantalla las edades contenidas.")
    print("3. Calcular la frecuencia de edad")
    print("0. Salir.")
    print()

def buttons(opcion):
    if opcion==1:
        load_Array(array)  
        print("Se han cargado exitosamente")
    elif opcion==2:
        display_Array(array)   
        print()
        print("Se han cargado exitosamente")
    elif opcion==3:
        frequency(array)
        
opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=int(input("Seleccione una opción (1-3): "))
    buttons(opcion)
    input("Presione Inter para continuar: ")
"""


#Vectores sobredimensionados

#Agregar un elemento del vector (Actualización)

import random
#array=[0]*9 #Este número No se modifica, al ser un vector estático
#cantidad_util=6
array=[0]*15
cantidad_util=10 

#Cargar el vector
for x in range(cantidad_util):
    array[x]=random.randint(1,10)

#Mostrar el vector
for x in range(cantidad_util):
    print(array[x],end=" ")


print()
numero=int(input("¿Que número desea agregar al vector?: ")) #9
array[cantidad_util]=numero #0 en la posicion 6, va a valer 9
cantidad_util=cantidad_util+1 #6=6+1 =7

for x in range(cantidad_util):
    print(array[x],end=" ")



#Eliminar un elemento del vector (Eliminación secuencial)

print()
opcion=input("¿Desea eliminar el último elemento del vector? (Si-No): ") #9
if opcion=="y":
    cantidad_util=cantidad_util-1 #6=6+1 =7
    
for x in range(cantidad_util):
    print(array[x],end=" ")

#Eliminar un elemento del vector (Eliminación aleatoria)

print()
numero=int(input("¿En que posición se encuentra el número que desea eliminar?: ")) #0
steps=cantidad_util-1 #5
steps=steps-numero #5-0   #5,4,3,2,1,0
for x in range(steps):
    array[numero]=array[numero]+array[numero+1]
    array[numero+1]=array[numero]-array[numero+1]
    array[numero]=array[numero]-array[numero+1]
    numero=numero+1
cantidad_util=cantidad_util-1

for x in range(cantidad_util):
    print(array[x],end=" ")


#Insertar un elemento del vector (Inserción)

"""
print()
numero=int(input("¿Que número desea insertar en el vector?: ")) #7
posicion=int(input("Bien, ¿En que posición desea agregar ese número?: ")) #2
steps=cantidad_util
steps=steps-posicion
lure=cantidad_util
for x in range(steps):
    array[lure]=array[lure]+array[lure-1]
    array[lure-1]=array[lure]-array[lure-1]
    array[lure]=array[lure]-array[lure-1]
    lure=lure-1
cantidad_util=cantidad_util+1
array[posicion]=numero

for x in range(cantidad_util):
    print(array[x],end=" ")






"""
"""
#4)

array=[0]*40

def load_Array(array):
   for x in range(40):
       array[x]=random.randint(-10,10)

def display_Array(array):
    for x in range(40):
        print(array[x],end=" ")

def sum15(array):
    for x in range(40):
        if array[x]<0:
            array[x]=array[x]+15

def repeat_Number(array):
    array2=[0]*21
    acumulador=0
    for x in range(40):
        posicion=array[x]
        array2[posicion]=array2[posicion]+1
        if array2[posicion]>1:
            array[x]=-1
            acumulador=acumulador+1
    return acumulador

#Menú Principal
def main_Menu():
    print("***MENU PRINCIPAL***")
    print()
    print("1. Cargar 40 números entre -10 y 10")
    print("2. Mostrar por pantalla las edades contenidas.")
    print("3. Eliminar los números negativos")
    print("4. Eliminar los números repetidos")
    print("0. Salir.")
    print()

def buttons(opcion):
    if opcion==1:
        load_Array(array)  
        print("Se han cargado exitosamente")
    elif opcion==2:
        display_Array(array)   
        print()
        print("Se han cargado exitosamente")
    elif opcion==3:
        sum15(array)
        print("Se han eliminado exitosamente")
    elif opcion==4:
        cantidad=repeat_Number(array)
        print("Se han modificado una cantidad de",cantidad,"repeticiones")

opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=int(input("Seleccione una opción (1-3): "))
    buttons(opcion)
    input("Presione Inter para continuar: ")
"""