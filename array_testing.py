



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


esta=False
while esta:
    print("!")


for x in range(12):
    suma=0
    if (x%2)==1:
        suma=suma+1

