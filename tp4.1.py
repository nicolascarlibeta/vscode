



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



busqueda=1110
def balance_inq(cuentas,busqueda):
    print("Su saldo actual es:  $",cuentas[busqueda-1000].sal)



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
    busqueda=input("Hola. Por favor, Ingrese su D.N.I.: ")
    termino=False
    while c<cant and not(termino):
        if busqueda==cuentas[c].identity:
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
        cuentas[cant].actype=int(input("Por favor, ingrese el tipo de cuenta: "))
        cuentas[-1].acnum=cuentas[-1].acnum+1
            

            
         #   if cuentas[c].active==False:
          #      print("La cuenta se encuentra actualmente DESACTIVADA. ¿Desea activarla?: ")
           #     termino=True

        


                #opcion=input("Seleccione una opción (S-N): ").upper()
                #if opcion=="S":
                 #   cuentas[c].active=True
                  #  print("La cuenta fue activada exitosamente")
                #else:
                 #   termino=True
            #else:


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

def buttons(opcion):
    #if opcion==1:
     #   load_Array(dockets,notes) 
      #  print("Se han cargado exitosamente")
    #if opcion==2:
     #   os.system("cls")
      #  print("PLANILLA COMPLETA: ")
       # display_Array(dockets,notes)   
        #print("Se han cargado exitosamente")
    if opcion==3:
        print("Legajos","Promedio")
        prmd=promedio(dockets,notes)
        display_Array2(dockets,prmd)
        print()
        print("Se han cargado exitosamente")


opcion=5
read_ac(cuentas)
while opcion!=0:
    os.system("cls")
    main_Menu()
    opcion=int(input("Seleccione una opción (1-0): "))
    buttons(opcion)
    input("Presione Inter para continuar: ")
                    


