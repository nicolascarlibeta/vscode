


import random

#-----------------------------------------------------------
# Opción 1

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

def one_Menu():
    print(" "*39,"★★★ OPCIÓN 1★★★")
    print()
    print(" "*25,"1. Cargar 250 números aleatorios entre -100 y 100.")
    print(" "*25,"2. Mostrar por pantalla los números contenidos.")
    print(" "*25,"3. Calcular la cantidad de números negativos, positivos y ceros.")
    print(" "*25,"4. Encontrar al número mas grande de todos.")
    print(" "*25,"5. Sumar los números con posiciones impares.")
    print(" "*25,"0. Salir.")
    print()

def buttons1():
    opcion=5
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


