


#Trabajo práctico 3

from pyrecord import Record
import numpy as np, os, random

#1)
"""
reg=Record.create_type("reg",
"docket",
"name",
"surname",
"notes",
docket=0,
name="",
surname="",
notes=0)

record=reg

recay=np.array([record]*10)

def load(array):
    numero=1
    nodes=np.array([0]*3)
    for x in range(len(array)):
        array[x]=reg()
        array[x].docket=array[x].docket+numero
        numero=numero+100
        array[x].notes=array[x].notes+nodes
        array[x].name=input("Por favor, ingrese un nombre: ")
        array[x].surname=input("Por favor, ingrese un apellido: ")
        array[x].notes[0]=int(input("Por favor, ingrese la nota 1: "))
        array[x].notes[1]=int(input("Por favor, ingrese la nota 2: "))
        array[x].notes[2]=int(input("Por favor, ingrese la nota 3: "))


def average(array,posicion):
    suma=0
    condicion=""
    for j in range(3):
        suma=suma+array[posicion].notes[j]
    promedio=suma/3

    if promedio>=7:
        condicion="Promovido"
    elif promedio>=4 and promedio<7:
        condicion="Regular"
    else:
        condicion="Libre"


    return promedio,condicion


def display(array):
    posicion=0
    for x in range(len(array)):
        promedio,condicion=average(recay,posicion)
        print(array[x].docket,array[x].name,array[x].surname,promedio,condicion)
        posicion=posicion+1


load(recay)
display(recay)
"""

#2)

reg=Record.create_type("reg",
"name",
"age",
"sex",
"civil",
"wage",
name="",
age=0,
sex="",
civil="",
wage=0.0)

record=reg

recarray=np.array([record]*3)


def load(array):
    for x in range(len(array)):
        array[x]=reg() #Inicializamos el vector
        array[x].name=input("Por favor, ingrese un nombre: ")
        array[x].age=int(input("Por favor, ingrese una edad: "))
        array[x].sex=input("Por favor, ingrese su sexo (F.Femenino-M.Masculino): ").upper()
        array[x].civil=input("Por favor, ingrese el estado civil (S.Soltero-C.Casado-D.Divorciado-O.Otro): ").upper()
        array[x].wage=float(input("Por favor, ingrese su salario base: "))


def display(array):
    for x in range(len(array)):
        print(array[x].name,array[x].age,array[x].sex,array[x].civil,array[x].wage)
        

def malemp(array):
    trabajadores=0
    for x in range(len(array)):
        if array[x].sex=="M":
            trabajadores=trabajadores+1

    return trabajadores


def marremp(array):
    casadas=0
    for x in range(len(array)):
        if array[x].sex=="F":
            if array[x].civil=="C":
                casadas=casadas+1

    return casadas


def youngemp(array):
    menor=array[0].age
    nombre=array[0].name
    for x in range(len(array)):     
        if array[x].age<menor:
            menor=array[x].age
            nombre=array[x].name
    
    return nombre
            

def sigwage(array):
    suma=0
    for x in range(len(array)):     
        suma=suma+array[x].wage
    
    return suma


def main_Menu():
    print("***MENU PRINCIPAL***")
    print()
    print("1. Cargar la planilla.")
    print("2. Mostrar los datos completos.")
    print("3. Calcular la cantidad de trabajadores de sexo masculino.")
    print("4. Calcular la cantidad de trabajadoras casadas.")
    print("5. Informar el nombre del empleado/a más joven.")
    print("6. Calcular la suma de todos los salarios.")
    print("0. Salir.")
    print()

def buttons(opcion):
    if opcion==1:
        load(recarray)  
        print("Se han cargado exitosamente")
    elif opcion==2:
        print()
        print("Nombre","Edad","Sexo","Estado Civil","Salario base")
        display(recarray)   
        print()
        print("Se han cargado exitosamente")
    elif opcion==3:
        male=malemp(recarray)
        print("La cantidad de trabajadores de sexo masculino es de: ",male)
    elif opcion==4:
        married=marremp(recarray)
        print("La cantidad de trabajadoras casadas es de: ",married)
    elif opcion==5:
        name=youngemp(recarray)
        print("El empleado/a más joven es: ",name)
    elif opcion==6:
        wage=sigwage(recarray)
        print("La suma de todos los salarios es de: ",wage)

opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=int(input("Seleccione una opción (1-3): "))
    buttons(opcion)
    input("Presione Inter para continuar: ")
