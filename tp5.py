



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

#3)

def write(variable,month,days,years,temp):
    for m in range(1):
        for d in range(1):
            writeline=str(days)+"-"+str(month)+"-"+str(years)+"-"+str(temp)+"\n"
            variable.write(writeline)
            
def readandwrite():
    celsius=open("temperaturas.txt","r")
    avg_celsius=open("temp_media.txt","w")
    readline=celsius.readline()
    temp_med=0
    while readline!="":
        s=readline.split("-") #Divide la lineas según el guión
        dia=int(s[0])
        mes=int(s[1])
        año=int(s[2])
        max=int(s[4])
        min=int(s[3])
        temp_med=(min+max)/2
        write(avg_celsius,mes,dia,año,temp_med)
        readline=celsius.readline()

    avg_celsius.close()
    celsius.close()


def read():
    avg_celsius=open("temp_media.txt","r")
    readline=avg_celsius.readline()
    while readline!="":
        s=readline.split("-") #Divide la lineas según el guión
        dia=int(s[0])
        mes=int(s[1])
        año=int(s[2])
        temp_med=float(s[3])
        print(" "*35,dia,mes,año,temp_med)
        readline=avg_celsius.readline()

    avg_celsius.close()



def main_Menu():
    print()
    print()
    print(" "*45,"Menú Principal")
    print()
    print(" "*35,"1 Leer y crear el archivo automáticamente.")
    print()
    print(" "*35,"2 Leer el archivo de temperaturas medias diarias.")
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
        readandwrite()
        spaces()
        print(" "*35,"Se ha creado exitosamente")
        spaces()
    elif opcion==2:
        os.system("cls")
        read()
        spaces()
        print(" "*35,"Se ha cargado exitosamente")


opcion=5
while opcion!=0:
    os.system("cls")
    main_Menu()
    print(" "*35,end="")
    opcion=int(input("Seleccione una opción: "))
    buttons(opcion)
    print(" "*35,end="")
    input("Presione Inter para continuar: ")


#----------------------------------------------------------------
#Ejercicios Adicionales


#1)

def write():
    quora=open("encuesta.txt","w")
    for q in range(20):
        sex=random.randint(1,2)
        age=random.randint(15,59)
        civil_state=random.randint(1,3)
        work=random.randint(0,1)
        study=random.randint(0,1)
        writeline=str(sex)+"-"+str(age)+"-"+str(civil_state)+"-"+str(work)+"-"+str(study)+"\n"
        quora.write(writeline)

    quora.close()

def read():
    quora=open("encuesta.txt","r")
    readline=quora.readline()
    vec_quora=np.array([0]*7)
    while readline!="":
        s=readline.split("-") #linea.separado por(coma, linea, punto, etc.)
        sex=int(s[0])
        age=int(s[1])
        cs=int(s[2])
        work=int(s[3])
        study=int(s[4])

        if sex==1:
            vec_quora[0]=vec_quora[0]+1
        else:
            vec_quora[1]=vec_quora[1]+1
        
        if age<18 and work==1:
            vec_quora[2]=vec_quora[2]+1

        if cs==1:
            vec_quora[3]=vec_quora[3]+1
        elif cs==2:
            vec_quora[4]=vec_quora[4]+1
        
        if work==1 and study==1:
            vec_quora[5]=vec_quora[5]+1

        if sex==2 and work==1:
            vec_quora[6]=vec_quora[6]+1
    
        readline=quora.readline()

    print(" "*35,"PORCENTAJES")
    print()
    print(" "*35,"Varones: ",vec_quora[0])
    print(" "*35,"Mujeres: ",vec_quora[1])
    print(" "*35,"Menores de 18 años que trabajan: ",vec_quora[2])
    print(" "*35,"Solteros: ",vec_quora[3])
    print(" "*35,"Casados: ",vec_quora[4])
    print(" "*35,"Encuestados que trabajan y estudian: ",vec_quora[5])
    print(" "*35,"Mujeres que trabajan: ",vec_quora[6])
    print()

    quora.close()


def main_Menu():
    print()
    print()
    print(" "*35,"Menú Principal")
    print()
    print(" "*25,"1 Cargar los datos de la encuesta.")
    print()
    print(" "*25,"2 Leer el archivo e informar un reporte de porcentajes.")
    print()
    print(" "*25,"0 Salir.")
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
        spaces()
        print(" "*35,"Se ha cargado exitosamente")


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

#2)

def read(g,p,m):
    store=open("productos.dat","r")
    readline=store.readline()
    grams=0
    while readline!="":
        s=readline.split(",")
        prod=int(s[0])
        mp=int(s[1])
        cant=float(s[2])
        cost=float(s[3])

        if prod==p:
            if mp==m:
                grams=100/cant
                grams=g/grams
                
        readline=store.readline()
    
    print(" "*20,"La cantidad de materia prima necesaria para fabricar",g,"gramos es de: ",grams)
    store.close()



regs=Record.create_type("regs",
"cant",
"mp",
cant=0.00,
mp=0)

mp=regs

mprim=np.array([mp]*6)

def load(rec):
    for x in range(len(rec)):
        rec[x]=regs()

def read2(rec):
    store=open("productos.dat","r")
    readline=store.readline()
    load(rec)
    while readline!="":
        s=readline.split(",")
        prod=int(s[0])
        mp=int(s[1])
        cant=float(s[2])

        if prod==6:
            if cant>rec[0].cant:
                rec[0].cant=cant
                rec[0].mp=mp
        elif prod==5:
            if cant>rec[1].cant:
                rec[1].cant=cant
                rec[1].mp=mp
        elif prod==4:
            if cant>rec[2].cant:
                rec[2].cant=cant
                rec[2].mp=mp
        elif prod==3:
            if cant>rec[3].cant:
                rec[3].cant=cant
                rec[3].mp=mp
        elif prod==2:
            if cant>rec[4].cant:
                rec[4].cant=cant
                rec[4].mp=mp
        elif prod==1:
            if cant>rec[5].cant:
                rec[5].cant=cant
                rec[5].mp=mp

        readline=store.readline()
    
    print(" "*35,"MATERIA PRIMA PRINCIPAL POR PRODUCTO")
    print()
    print(" "*35,"Producto N°1: ","Materia Prima N°"+str(rec[5].mp))
    print(" "*35,"Producto N°2: ","Materia Prima N°"+str(rec[4].mp))
    print(" "*35,"Producto N°3: ","Materia Prima N°"+str(rec[3].mp))
    print(" "*35,"Producto N°4: ","Materia Prima N°"+str(rec[2].mp))
    print(" "*35,"Producto N°5: ","Materia Prima N°"+str(rec[1].mp))
    print(" "*35,"Producto N°6: ","Materia Prima N°"+str(rec[0].mp))
    print()

    store.close()



def read3():
    store=open("productos.dat","r")
    readline=store.readline()
    vec_cost=np.array([0.0]*6)
    while readline!="":
        s=readline.split(",")
        prod=int(s[0])
        mp=int(s[1])
        cant=float(s[2])
        cost=float(s[3])

        if prod==6:
            vec_cost[0]=vec_cost[0]+cost
        elif prod==5:
            vec_cost[1]=vec_cost[1]+cost
        elif prod==4:
            vec_cost[2]=vec_cost[2]+cost
        elif prod==3:
            vec_cost[3]=vec_cost[3]+cost
        elif prod==2:
            vec_cost[4]=vec_cost[4]+cost
        elif prod==1:
            vec_cost[5]=vec_cost[5]+cost


        readline=store.readline()

    for j in range(len(vec_cost)):
        vec_cost[j]=vec_cost[j]/3

    print(" "*35,"COSTO PROMEDIO POR PRODUCTO")
    print()
    print(" "*35,"Producto N°1: ","Costo Promedio (en pesos): ",vec_cost[5])
    print(" "*35,"Producto N°2: ","Costo Promedio (en pesos): ",vec_cost[4])
    print(" "*35,"Producto N°3: ","Costo Promedio (en pesos): ",vec_cost[3])
    print(" "*35,"Producto N°4: ","Costo Promedio (en pesos): ",vec_cost[2])
    print(" "*35,"Producto N°5: ","Costo Promedio (en pesos): ",vec_cost[1])
    print(" "*35,"Producto N°6: ","Costo Promedio (en pesos): ",vec_cost[0])
    print()

    store.close()



def main_Menu():
    print()
    print()
    print(" "*35,"Menú Principal")
    print()
    print(" "*20,"1 Calcular la cantidad de materia prima mecesaria para fabricar n gramos de n producto.")
    print()
    print(" "*20,"2 Mostrar por cada producto su materia prima principal.")
    print()
    print(" "*20,"3 Mostrar el costo promedio por producto.")
    print()
    print(" "*20,"0 Salir.")
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
        grams=float(input("Por favor, ingrese los gramos correspondientes: "))
        product=int(input("Por favor, ingrese el producto correspondiente: "))
        mp=int(input("Por favor, ingrese la materia prima correspondiente: "))
        os.system("cls")
        spaces()
        read(grams,product,mp)
        spaces()
    elif opcion==2:
        os.system("cls")
        read2(mprim)
        spaces()
    elif opcion==3:
        os.system("cls")
        read3()
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





