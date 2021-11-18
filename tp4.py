



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


def concut():
    query=open("informe.txt","r")
    linea=query.readline().strip()
    s=linea.split("-")
    branch=int(s[1])
    dept=int(s[2])
    print(" "*35,"REPORTE DE SUELDOS")
    while linea!="":
        suma=0
        prev_branch=branch
        print(" "*35,"SUCURSAL",prev_branch)
        print(" "*35,"Dept.","Cod.","Sueldo")
        while prev_branch==branch and linea!="":
            prev_dept=dept 
            suma2=0
            while prev_dept==dept and linea!="":
                emp=int(s[0])
                salary=int(s[3])
                suma2=suma2+salary # Total de sueldos x departamento
                suma=suma+salary # Total de sueldos x sucursal
                print(" "*35,dept,emp,salary)
                linea=query.readline().strip()
                if linea!="":
                    s=linea.split("-")
                    branch=int(s[1])
                    dept=int(s[2])
        
            print(" "*35,"TOTAL DE DEPARTAMENTO:     ",suma2)
        
        print(" "*35,"TOTAL DE SUCURSAL:       ",suma)
        print()

    query.close()



def main_Menu():
    print()
    print()
    print(" "*45,"Menú Principal")
    print()
    print(" "*30,"1 Cargar los datos correspondientes.")
    print()
    print(" "*30,"2 Leer e informar un reporte de sueldos totales por sucursal y por departamento.")
    print()
    print(" "*30,"0 Salir.")
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
        concut()
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

def write():
    customers=open("clientes.dat","w")
    index=open("movimientos.dat","w")
    acnum=45000
    for c in range(6):
        acnum=acnum+1
        ccode=random.randint(10300,10399)
        sal=random.randint(-5000,5000)
        linea=str(acnum)+"."+str(ccode)+"."+str(sal)+"\n"
        customers.write(linea)
        for m in range(2):
            mov=random.randint(1,2)
            imp=random.randint(100,5000)
            linea=str(acnum)+"."+str(mov)+"."+str(imp)+"\n"
            index.write(linea)

    customers.close()
    index.close()

           
def read():
    customers=open("clientes.dat","r")
    index=open("movimientos.dat","r")
    linea=customers.readline().strip()
    linea2=index.readline().strip()
    sep=linea2.split(".")
    acnum=int(sep[0])
    print(" "*43,"MOVIMIENTOS")
    print()
    while linea2!="":
        s=linea.split(".")
        prev_acnum=acnum
        account=int(s[0])
        ccode=int(s[1])
        sal=int(s[2])
        print(" "*35,"Número de cuenta: ",prev_acnum)
        print(" "*35,"Código de cliente: ",ccode)
        if prev_acnum==account:
            while prev_acnum==acnum and linea2!="":
                mov=int(sep[1])
                imp=int(sep[2])
            
                if mov==1:
                    sal=sal+imp
                else:
                    sal=sal-imp
                
                linea2=index.readline().strip()

                if linea2!="":
                    sep=linea2.split(".")
                    acnum=int(sep[0])
            
                print(" "*35,"Tipo de movimiento: "+str(mov)+" - "+"Importe: "+str(imp))
        print()
        
        linea=customers.readline().strip()

        
    customers.close()
    index.close()




def main_Menu():
    print()
    print()
    print(" "*45,"Menú Principal")
    print()
    print(" "*30,"1 Cargar los datos correspondientes.")
    print()
    print(" "*30,"2 Leer e informar un listado de ultimos movimientos.")
    print()
    print(" "*30,"0 Salir.")
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

#4)

def write():
    indec=open("indec.dat","w")
    prov=0
    for p in range(5):
        prov=prov+1
        ciud=0
        for c in range(2):
            ciud=ciud+1
            v=random.randint(3000,5000)
            m=random.randint(3000,5000)
            d=random.randint(300,500)
            linea=str(prov)+"-"+str(ciud)+"-"+str(v)+"-"+str(m)+"-"+str(d)+"\n"
            indec.write(linea)

    indec.close()

def control_cut():
    indec=open("indec.dat","r")
    linea=indec.readline().strip()
    s=linea.split("-")
    prov=int(s[0])
    mayor_prov=0
    provincia=0
    while linea!="":
        suma=0
        suma2=0
        prev_prov=prov
        while prev_prov==prov and linea!="":
            ciud=int(s[1])
            v=int(s[2])
            m=int(s[3])
            d=int(s[4])
            suma=suma+v+m
            suma2=suma2+d

            if suma2>mayor_prov:
                mayor_prov=suma2
                provincia=prov
            
            linea=indec.readline()
            if linea!="":
                s=linea.split("-")
                prov=int(s[0])

        print(provincia)

    indec.close()

control_cut()

            
            
            
            








        