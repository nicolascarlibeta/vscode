



#Trabajo práctico 5

import os, random, numpy as np
from pyrecord import Record

#1)
"""
def write():
    fluvial=open("lluvias.txt","w")
    dia=0
    for w in range(30):
        dia=dia+1
        mes=9
        año=2021
        precipitaciones=random.randint(0,95)
        linea=str(dia)+"-"+str(mes)+"-"+str(año)+"-"+str(precipitaciones)+"\n"
        fluvial.write(linea)

    fluvial.close()


def read():
    fluvial=open("lluvias.txt","r")
    linea=fluvial.readline().strip()
    dwr=0
    mayor=0
    menor=0
    print(" "*20,"Dia     Més     Año       Precipitaciones")
    while linea!="": #Se corta el ciclo una vez que no encuentre mas lineas
        s=linea.split("-") #Esto divide o separa la linea de sus elementos
        dia=int(s[0]) #Una vez separados sus elementos, los guardamos en listas para utilizarlos individualmente
        mes=int(s[1]) 
        año=int(s[2])
        precipitaciones=int(s[3])
        if precipitaciones==0:
            dwr=dwr+1
        elif precipitaciones>=50:
            mayor=mayor+1
        else:
            menor=menor+1
        print(f'{dia:>20} {mes:>20} {año:>20} {precipitaciones:>20}')
        linea=fluvial.readline().strip()

    print()
    print(" "*35,"Cantidad de dias sin precipitaciones de lluvia: ",dwr)
    print()
    print(" "*35,"Cantidad de dias con precipitaciones mayores o iguales a 50 mm: ",mayor)
    print()
    print(" "*35,"Cantidad de dias con precipitaciones menores a 50 mm: ",menor)

    fluvial.close()


def main_Menu():
    print()
    print()
    print(" "*45,"Menú Principal")
    print()
    print(" "*35,"1 Crear el archivo automáticamente.")
    print()
    print(" "*35,"2 Leer el archivo e informar el estado actual de precipitaciones.")
    print()
    print(" "*35,"0 Salir.")
    print()
    print()

def spaces():
    print()
    print()
    print()
    print()
    print()
    print()
    print()

def buttons(opcion):
    if opcion==1:
        os.system("cls")
        write()
        spaces()
        print(" "*35,"Se ha creado exitosamente")
        spaces()
    elif opcion==2:
        os.system("cls")
        read()
        spaces()
        print(" "*35,"Se ha cargado exitosamente")
        spaces()


opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    print(" "*35,end="")
    opcion=int(input("Seleccione una opción: "))
    buttons(opcion)
    print(" "*35,end="")
    input("Presione Inter para continuar: ")


#2)


def write():
    celsius=open("temperaturas.txt","w")
    mes=0
    for m in range(12):
        mes=mes+1
        dia=0
        for d in range(30):
            dia=dia+1
            año=2021
            max=random.randint(20,35)
            min=random.randint(1,19)
            linea=str(dia)+"-"+str(mes)+"-"+str(año)+"-"+str(min)+"-"+str(max)+"\n" #Agregamos los datos
            celsius.write(linea)

    celsius.close()



def read():
    celsius=open("temperaturas.txt","r")
    linea=celsius.readline()
    s=linea.split("-")
    min=int(s[3])
    vec_min=np.array([min,0,0])
    vec_max=np.array([0,0,0])
    menor_temp=0
    for a in range(360):
        s=linea.split("-")
        dia=int(s[0])
        mes=int(s[1])
        max=int(s[4])
        min=int(s[3])

        if min<vec_min[0]:
            vec_min[0]=min
            vec_min[1]=dia
            vec_min[2]=mes

        elif max>vec_max[0]:
            vec_max[0]=max
            vec_max[1]=dia
            vec_max[2]=mes
            menor_temp=min

        linea=celsius.readline()
    
    amp=vec_max[0]-menor_temp

    print(" "*35,"TEMPERATURA: INFORME ANUAL")
    print()
    print(" "*35,"Temperatura Mínima del año: ",vec_min[0])
    print(" "*35,"Registrada el Día: ",vec_min[1])
    print(" "*35,"Del Mes: ",vec_min[2])
    print()
    print(" "*35,"Temperatura Máxima del año: ",vec_max[0])
    print(" "*35,"Registrada el Día: ",vec_max[1])
    print(" "*35,"Del Mes: ",vec_max[2])
    print()
    print(" "*35,"Máxima Amplitud Térmica: ",amp)
    print(" "*35,"Registrada el Día: ",vec_max[1])
    print(" "*35,"Del Mes: ",vec_max[2])
    print()

    celsius.close()


           
def main_Menu():
    print()
    print()
    print(" "*45,"Menú Principal")
    print()
    print(" "*35,"1 Crear el archivo automáticamente.")
    print()
    print(" "*35,"2 Leer el archivo e informar un reporte anual de temperaturas.")
    print()
    print(" "*35,"0 Salir.")
    print()
    print()

def spaces():
    print()
    print()
    print()
    print()
    print()
    print()
    print()

def buttons(opcion):
    if opcion==1:
        os.system("cls")
        write()
        spaces()
        print(" "*35,"Se ha creado exitosamente")
        spaces()
    elif opcion==2:
        os.system("cls")
        spaces()
        read()
        print(" "*35,"Se ha cargado exitosamente")
        spaces()


opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    print(" "*35,end="")
    opcion=int(input("Seleccione una opción: "))
    buttons(opcion)
    print(" "*35,end="")
    input("Presione Inter para continuar: ")
"""