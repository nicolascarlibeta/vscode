



#Trabajo Práctico de Registros y Corte de Control



from pyrecord import Record
import os, random, numpy as np

regc=Record.create_type("regc",
"acnum",
"sur",
"name",
"identity",
"actype",
"sal",
"active",
acnum=0,
sur="",
name="",
identity="",
actype=0,
sal=0.0,
active=True)

regb=Record.create_type("regb",
"num",
"ubi",
"mov",
num=0,
ubi="",
mov=0)

ac=regc
atm=regb

cuentas=np.array([ac]*610)
cajeros=np.array([atm]*120)

#Carga de vector de Cuentas

def read_ac(cuentas):
    clientes=open("cuentas.txt","r")
    linea=clientes.readline().strip()
    cant=600
    for c in range(cant):
        s=linea.split(",")
        n=int(s[0])
        sur=s[1]
        name=s[2]
        identity=s[3]
        t=int(s[4])
        sal=float(s[5])
        a=bool(s[6])

        #Carga del vector de registros
        cuentas[c]=regc()
        cuentas[c].acnum=n
        cuentas[c].sur=sur
        cuentas[c].name=name
        cuentas[c].identity=identity
        cuentas[c].actype=t
        cuentas[c].sal=sal
        cuentas[c].active=a

        linea=clientes.readline().strip()
        

    cuentas[-1]=regc()
    cuentas[-1].acnum=cant #Cantidad útil

    clientes.close()

#Carga de vector de Cuentas

def read_atm(cajeros):
    caja=open("cajeros.txt","r")
    linea=caja.readline().strip()
    j=0
    while linea!="":
        s=linea.split(",")
        num=int(s[0])
        ubi=s[1]
        mov=int(s[2])

        #Carga del vector de registros
        cajeros[j]=regb()
        cajeros[j].num=num
        cajeros[j].ubi=ubi
        cajeros[j].mov=mov

        j=j+1
        
        linea=caja.readline().strip()

    caja.close()


def balance_inq(cuentas,busqueda):
    busqueda=busqueda-1000
    if busqueda<cuentas[-1].acnum:
        print()
        print("N° de Cuenta: ",cuentas[busqueda].acnum)
        print("Apellido: ",cuentas[busqueda].sur)
        print("Nombre: ",cuentas[busqueda].name)
        print("D.N.I.: ",cuentas[busqueda].identity)
        print("Su saldo actual es:  $",cuentas[busqueda].sal)
        print()
    else:
        print("No tenemos registro de este número de cuenta en nuestro banco.")



#Corte de control

def amount(cuentas):
    operaciones=open("operaciones.txt","r")
    linea=operaciones.readline().strip()
    s=linea.split(",")
    acnum=int(s[0])
    while linea!="":
        suma=0
        prev_acnum=acnum
        c=prev_acnum-1000
        while acnum==prev_acnum and linea!="":
            a=int(s[1])
            m=int(s[2])
            d=int(s[3])
            c=int(s[4])
            mov=int(s[5])
            b=float(s[6])

            if mov==1:
                suma=suma+b
            else:
                suma=suma-b

            linea=operaciones.readline().strip()
            if linea!="":
                s=linea.split(",")
                acnum=int(s[0])

        cuentas[c].sal=cuentas[c].sal+suma
        print("Número de Cuenta: ",prev_acnum)
        print("Total anual:  $",suma)
        print()

        c=c+1

    operaciones.close()



def amount_mov():
    operaciones=open("operaciones.txt","r")
    linea=operaciones.readline().strip()
    s=linea.split(",")
    acnum=int(s[0])
    while linea!="":
        2


#Altas, Bajas y Modificaciones (ABM)

def display_ac(cuentas,c):
    print()
    print("N° de Cuenta: ",cuentas[c].acnum)
    print("Apellido: ",cuentas[c].sur)
    print("Nombre: ",cuentas[c].name)
    print("D.N.I.: ",cuentas[c].identity)
    print("Tipo de Cuenta: ",cuentas[c].actype)
    print("Saldo:  $",cuentas[c].sal)
    

def register(cuentas):
    c=0
    cant=cuentas[-1].acnum
    identity=input("Hola. Por favor, Ingrese su D.N.I.: ")
    termino=False
    while c<cant and not(termino):
        if identity==cuentas[c].identity:
            if cuentas[c].active==False:
                print("La cuenta se encuentra actualmente DESACTIVADA. ¿Desea activarla?: ")
                opcion=input("Seleccione una opción (S-N): ").upper()
                if opcion=="S":
                    cuentas[c].active=True
                    print("La cuenta fue activada exitosamente")
                
            else:    
                print()
                print("El cliente ya tiene una cuenta registrada.")
                print("Sus datos son los siguientes: ")
                display_ac(cuentas,c)
        
            termino=True

        c=c+1

    if not(termino):
        cuentas[cant]=regc()
        cuentas[cant].acnum=cuentas[cant-1].acnum+1
        cuentas[cant].sur=input("Por favor, ingrese su apellido: ").upper()
        cuentas[cant].name=input("Por favor, ingrese su nombre: ").upper()
        cuentas[cant].identity=identity        
        cuentas[cant].actype=int(input("Por favor, ingrese el tipo de cuenta: "))
        cuentas[-1].acnum=cuentas[-1].acnum+1    
        display_ac(cuentas,cant)
        print("La cuenta ha sido creada exitosamente")
            

def cancellation(cuentas):
    busqueda=int(input("Por favor, ingrese el NÚMERO DE CUENTA que desea dar de baja: "))
    if cuentas[busqueda-1000].active==False:
        print("Esta cuenta ya se encuentra ACTUALMENTE dada de baja")
    else:
        cuentas[busqueda-1000].active=False
        print("La cuenta N° "+str(busqueda)+" ("+str(cuentas[busqueda-1000].sur)+", "+str(cuentas[busqueda-1000].name)+")"+" fue desactivada exitosamente")


def modification(cuentas):
    opcion=5
    num=int(input("Hola, por favor Ingrese el NÚMERO DE CUENTA que desea modificar: "))-1000
    print()
    print("Estos son los datos actuales: ")
    display_ac(cuentas,num)
    print()
    print("Seleccione el campo que desea modificar: ")
    print()
    print("1. APELLIDO.")
    print("2. NOMBRE.")
    print("3. D.N.I..")
    print("4. TIPO DE CUENTA.")
    print("0. Volver al menú principal.")
    print()
    opcion=int(input("Seleccione una opción (0-4): "))
    if opcion==1:
        cuentas[num].sur=input("Por favor, Ingrese el NUEVO Apellido: ").upper()
    elif opcion==2: 
        cuentas[num].name=input("Por favor, Ingrese el NUEVO Nombre: ").upper()
    elif opcion==3:
        cuentas[num].identity=input("Por favor, Ingrese el NUEVO D.N.I.: ").upper()
    elif opcion==4:
        cuentas[num].actype=int(input("Por favor, Ingrese el NUEVO Tipo de cuenta: "))
    
    if opcion!=0:
        print("Estos son los datos actuales: ")
        display_ac(cuentas,num)
        print("La cuenta ha sido modificada exitosamente")



def main_Menu():
    print("***MENU PRINCIPAL***")
    print()
    print("1. Consulta de Saldo.")
    print("2. Mostrar legajos y notas correspondientes.")
    print("3. Realizar ABM sobre CUENTAS.")
    print("0. Salir.")
    print()

def main_Menu_ABM():
    print("***MENU PRINCIPAL***")
    print()
    print("1. Realizar un alta de cuenta.")
    print("2. Realizar una baja de cuenta.")
    print("3. Realizar una modificación en cuenta.")
    print("0. Salir.")
    print()

def buttons_abm(opcion):
    if opcion==1:
        register(cuentas)
    elif opcion==2:
        cancellation(cuentas)
    elif opcion==3:
        modification(cuentas)

def buttons(opcion):
    if opcion==1:
        busqueda=int(input("Hola, por favor Ingrese el NÚMERO DE CUENTA: "))
        balance_inq(cuentas,busqueda)
    elif opcion==3:
        op_abm=5
        while op_abm!=0:
            os.system("cls")
            main_Menu_ABM()
            op_abm=int(input("Seleccione una opción (0-3): "))
            buttons_abm(op_abm)
    elif opcion==5:
        amount(cuentas)
        
opcion=5
read_ac(cuentas)
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=int(input("Seleccione una opción (0-3): "))
    buttons(opcion)
    input("Presione Inter para continuar: ")
                    


