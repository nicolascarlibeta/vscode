


#Trabajo Práctico 1.1 - Busqueda Binaria y Burbujeo

#Calcular el medio y preguntar si coinciden
#Sino, preguntar si es mayor o es menor
#Dependiendo de lo que sea, se descartan los otros números
#El medio sucede a otro

#Buscamos el número 19


#Calcular el medio: (p1+pf)//2

#def binary_Search(array,busqueda):
#    posicion1=0
#    posicionf=len(array)-1
#    termino=False
#    while (posicion1<=posicionf) and termino==False:
#        medium=posicion1+posicionf//2
#        if busqueda==array[medium]:
#        #Crear un flag o bandera, indicando un valor T o F
#            termino=True
#
#        elif busqueda>array[medium]:
#            posicion1=medium+1
#    
#        else:
#            posicionf=medium-1
#    
#    return termino


#binary_Search(array,busqueda)


#1)

import random, os


array=[1,3,5,7,9,11,13,15,17,19]
busqueda=int(input("Buscar por número...: "))

def binary_Search(array,busqueda):
    posicion1=0
    posicionf=len(array)-1
    termino=False
    while (posicion1<=posicionf) and termino==False:
        medium=(posicion1+posicionf)//2
        if busqueda==array[medium]:
        #Crear un flag o bandera, indicando un valor T o F
            termino=True

        elif busqueda>array[medium]:
            posicion1=medium+1 
    
        else:
            posicionf=medium-1

    if termino==True:
        return medium
    else:
        return -1

posicion=binary_Search(array,busqueda)
print("La posición en la que se encuentra el",busqueda,"es " +str(posicion)+ "°")



#
##Preguntar, si el número es mayor al número
##Si es asi, se intercambian los números
##Repetir la cantidad de veces igualada a la cantidad de elementos
#
##2)
#
#
#array=[0]*9
#
#def load_Array(array):
#    for x in range(9):
#        array[x]=random.randint(0,10)
#
#def display_Array(array):
#    for x in range(9):
#        print(array[x], end=" ")
#
#def bubble_Dazzle(array):
#    lenght=len(array)-1
#    lenght1=len(array)
#    for x in range(lenght): #1 - una pasada
#        #a)
#        lenght1=lenght1-1
#        for x in range(lenght1): #8
#            if array[x]>array[x+1]:
#                array[x]=array[x]+array[x+1] #De esta forma, se intercambian los valores (10=10+4 14)
#                array[x+1]=array[x]-array[x+1] #El valor 4, se resta entre el 14 y el 4 #10
#                array[x]=array[x]-array[x+1] #El valor 14, se resta con el número anterior #4
#      #el contador esta antes del ciclo del for, ya que si estuviera en esta linea, se ejecutaria como si fuese un else       
#      
#    #b)
def bubble_Dazzle2(array):
    lenght1=len(array)
    ciclos=True
    while ciclos: #1 - una pasada
        lenght1=lenght1-1
        ciclos=False
        for x in range(lenght1):
            if array[x]>array[x+1]: 
                array[x]=array[x]+array[x+1] #De esta forma, se intercambian los valores (10=10+4 14)
                array[x+1]=array[x]-array[x+1] #El valor 4, se resta entre el 14 y el 4 #10
                array[x]=array[x]-array[x+1] #El valor 14, se resta con el número anterior #4
                ciclos=True
#            
#            #if ciclos==-1:
#             #   termino=True
#    
#           #tenemos que dejar que haga una vuelta, aunque sea redundante.
#           
#
#def main_Menu():
#    print("***MENU PRINCIPAL***")
#    print()
#    print("1. Cargar el vector.")
#    print("2. Mostrar por pantalla el vector.")
#    print("3. Ordenar el vector.")
#    print("0. Salir.")
#    print()
#
#def buttons(opcion):
#    if opcion==1:
#        load_Array(array)  
#        print("Se han cargado exitosamente")
#    elif opcion==2:
#        display_Array(array)   
#        print()
#        print("Se han cargado exitosamente")
#    elif opcion==3:
#        #bubble_Dazzle(array)
#        bubble_Dazzle2(array)
#        print("Se ha ordenado exitosamente")
#
#opcion=5
#while opcion!=0:
#    os.system("cls")
#    main_Menu()
#    opcion=int(input("Seleccione una opción (1-3): "))
#    buttons(opcion)
#    input("Presione Inter para continuar: ")
#

#----------------------------------------------------
#Consignas mixtas


#array=[0]*1000
array=[0]*100000

def load_Array(array):
    for x in range(len(array)):
        array[x]=random.randint(1,115)

def display_Array(array):
    for x in range(len(array)):
        print(array[x], end=" ")

def main_Menu():
    print("***MENU PRINCIPAL***")
    print()
    print("1. Cargar el vector.")
    print("2. Mostrar por pantalla el vector.")
    print("3. Ordenar el vector.")
    print("4. Buscar en el vector ordenado.")
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
        bubble_Dazzle2(array)
        print("Se ha ordenado exitosamente")
    elif opcion==4:
        busqueda=int(input("Buscar por número...: "))
        binary_Search(array,busqueda)
        posicion=binary_Search(array,busqueda)
        print("La posición en la que se encuentra el",busqueda,"es " +str(posicion)+ "°")

opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=int(input("Seleccione una opción (1-3): "))
    buttons(opcion)
    input("Presione Inter para continuar: ")

















