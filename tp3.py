


#Trabajo práctico 3

from numpy.core.fromnumeric import transpose
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
"""

#----------------------------------------------------------------
#Ejercicios Adicionales


#1)

regc=Record.create_type("regc",
"level",
"prof",
level=0,
prof="")

clss=regc

classroom=np.array([clss]*5)

regs=Record.create_type("regs",
"name",
"sur",
"date",
"notes",
name="",
sur="",
date="",
notes=0)

stds=regs

stu=np.array([[stds]*20]*5)

def load_stu(struct):
    filas=struct.shape[0]
    columnas=struct.shape[1]
    name=["Jason","Kendrick","Laurence","Patrick","Sheila","Aubrey","Patricia","Brent"]
    sur=["O'Collins","Bergman","Idle","Jones","Cleese","Ryder","Peterson","Grundy","LaFerrere"]
    date=["29/7/2000","9/3/2002","10/8/2001","12/3/2004","21/9/2002","5/5/2002"]
    notes=np.array([0]*10)
    for f in range(filas):
        for c in range(columnas):
            struct[f,c]=regs()
            struct[f,c].name=random.choice(name)
            struct[f,c].sur=random.choice(sur)
            struct[f,c].date=random.choice(date)
            struct[f,c].notes=struct[f,c].notes+notes
            for n in range(len(notes)):
                struct[f,c].notes[n]=random.randint(1,10)


def load(array):
    prof=["Terry","Susan","Clementina","Foster","Graham","John","Adelaide","Brick"]
    for x in range(len(array)):
        array[x]=regc()
        array[x].level=random.randint(1,6)
        array[x].prof=random.choice(prof)                                            


def display_stu(struct):
    filas=struct.shape[0]
    columnas=struct.shape[1]
    for f in range(filas):
        for c in range(columnas):                               
            print(struct[f,c].name,end=" ")
            print(struct[f,c].sur,end=" ")
            print(struct[f,c].date,end=" ")
            for n in range(10):
                print(struct[f,c].notes[n],end=" ")
            print()
        print()


def display_stu_notes(struct):
    filas=struct.shape[0]
    columnas=struct.shape[1]
    for f in range(filas):
        for c in range(columnas):                               
            print(struct[f,c].name,end=" ")
            print(struct[f,c].sur,end=" ")
            for n in range(10):
                print(struct[f,c].notes[n],end=" ")
            print()
        print()


def display(array):
    for x in range(len(array)):                             
        print(array[x].level,array[x].prof)

def sorting(struct):
    filas=struct.shape[0]
    columnas=struct.shape[1]
    for f in range(filas):
        for c in range(columnas):                               
            print(struct[f,c].name,end=" ")
            print(struct[f,c].sur,end=" ")
            for n in range(10):
                print(struct[f,c].notes[n],end=" ")
            print()
        print()





def main_Menu():
    print("***MENU PRINCIPAL***")
    print()
    print("1. Cargar la planilla.")
    print("2. Mostrar por los estudiantes por clase y sus respectivas notas.")
    print("3. Calcular la cantidad de trabajadores de sexo masculino.")
    print("0. Salir.")
    print()

def buttons(opcion):
    if opcion==1:
        load(classroom)  
        load_stu(stu)  
        print("Se han cargado exitosamente")
    elif opcion==2:
        display_stu_notes(stu)

opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=int(input("Seleccione una opción (1-3): "))
    buttons(opcion)
    input("Presione Inter para continuar: ")
