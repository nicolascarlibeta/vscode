



#Trabajo Práctico 4

import os, random

#1)
"""
def write():
    report=open("reporte.txt","w")
    branch=0
    for b in range(10):
        branch=branch+1
        for e in range(7):
            emp=random.randint(1001,1501)
            sal=random.randint(2000,5000)
            writeline=str(emp)+"-"+str(branch)+"-"+str(sal)+"\n"
            report.write(writeline)
    
    report.close()

    
def control_cut():
    report=open("reporte.txt","r")
    readline=report.readline().strip()
    s=readline.split("-")
    branch=int(s[1]) #Alojamos el primer valor del campo agrupado
    print(" "*35,"REPORTE DE SUELDO")
    while readline!="":
        suma=0 #se inicializa en cero por cada sucursal
        prev_branch=branch #Guardamos ese primer valor en una variable
        print(" "*35,"SUCURSAL",prev_branch)
        print(" "*35,"Código de Empleado","Sueldo")
        while readline!="" and branch==prev_branch:
            #Split a lo último
            emp=int(s[0])
            #sucursal a lo último
            salary=int(s[2])
            print(" "*35,emp,"$",salary)
            suma=suma+salary
            readline=report.readline().strip()
            if readline!="":
                s=readline.split("-")
                branch=int(s[1])
        print(" "*35,"TOTAL DE SUCURSAL:     ",suma)
        print()
    
    report.close()



def main_Menu():
    print()
    print()
    print(" "*45,"Menú Principal")
    print()
    print(" "*35,"1 Cargar los datos correspondientes.")
    print()
    print(" "*35,"2 Leer e informar un reporte de sueldos totales por sucursal.")
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
        control_cut()
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

#2)


def write():
    query=open("informe.txt","w")
    branch=0
    dept=40
    for b in range(6):
        branch=branch+1
        dept=dept*2
        for e in range(4):
            emp=random.randint(1001,2000)
            sal=random.randint(2000,5000)
            if e==2:
                dept=dept+1
            linea=str(emp)+"-"+str(branch)+"-"+str(dept)+"-"+str(sal)+"\n"
            query.write(linea)
        
    query.close()


def cc():
    query=open("informe.txt","r")
    linea=query.readline().strip()
    s=linea.split("-")
    branch=int(s[1])
    dept=int(s[2])
    while linea!="":
        suma=0
        prev_branch=branch
        prev_dept=dept
        while prev_branch==branch and linea!="":
            emp=int(s[0])
            salary=int(s[1])
            suma=suma+salary # Totál de sueldos x sucursal
            print("Departamento","Código de Empleado","Sueldo")
            suma2=0
            linea=query.readline().strip()
            while prev_dept==dept and linea!="":
                suma2=suma2+salary
                linea=query.readline().strip()
                if linea!="":
                    s=linea.split("-")
                    branch=int(s[1])
                    dept=int(s[2])
            
            print("Total por departamento",suma2)
        
        print("Total por sucursal",suma)

    query.close()


cc()

                
                

        