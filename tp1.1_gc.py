


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
input()


#2)


array=[0]*9

def load_Array(array):
    for x in range(9):
        array[x]=random.randint(0,10)

def display_Array(array):
    for x in range(9):
        print(array[x], end=" ")
""" 
def bubble_Dazzle(array):
    lenght=len(array)-1
    lenght1=len(array)
    for x in range(lenght): #1 - una pasada
        #a)
        lenght1=lenght1-1
        for x in range(lenght1): #8
            if array[x]>array[x+1]:
                array[x]=array[x]+array[x+1] #De esta forma, se intercambian los valores (10=10+4 14)
                array[x+1]=array[x]-array[x+1] #El valor 4, se resta entre el 14 y el 4 #10
                array[x]=array[x]-array[x+1] #El valor 14, se resta con el número anterior #4
"""         #el contador esta antes del ciclo del for, ya que si estuviera en esta linea, se ejecutaria como si fuese un else       
      
    #b)
def bubblelizer(array):
    lenght1=len(array)-1
    termino=False    
    while termino==False: #1 - una pasada
        lenght1=lenght1-1
        for x in range(lenght1): #8
            if array[x]>array[x+1]:
                array[x]=array[x]+array[x+1] #De esta forma, se intercambian los valores (10=10+4 14)
                array[x+1]=array[x]-array[x+1] #El valor 4, se resta entre el 14 y el 4 #10
                array[x]=array[x]-array[x+1] #El valor 14, se resta con el número anterior #4




           

def main_Menu():
    print("***MENU PRINCIPAL***")
    print()
    print("1. Cargar el vector.")
    print("2. Mostrar por pantalla el vector.")
    print("3. Ordenar el vector.")
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
        #bubble_Dazzle(array)
        bubblelizer(array)
        print("Se ha ordenado exitosamente")

opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=int(input("Seleccione una opción (1-3): "))
    buttons(opcion)
    input("Presione Inter para continuar: ")










