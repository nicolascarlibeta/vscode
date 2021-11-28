
from pyrecord import Record
import numpy as np



#Registro
record=Record.create_type("record","names","surnames","theorical","practical",names="",surnames="",theorical=0.0,practical=0)

#registro=función de registro(campos(nombres de variables),campos(variables y su tipo))
#Guardamos el TAD Registro en una variable
recordio=record #-------Variable de registro 
"""
recordio.names="Cristoforo" #------Accedo al campo "names" y le asigno un valor
recordio.surnames="Lagguard" #----Accedo al campo "surnames" y le asigno un valor
recordio.theorical=7.9 #------Accedo al campo "theorical" y le asigno un valor
recordio.practical=8.5 #------Accedo al campo "practical" y le asigno un valor
"""
#print(recordio.names,recordio.surnames,recordio.theorical,recordio.practical)


#¿Como creamos un vector de registros?
#array=np.array([0]*5) #----Vector
recarray=np.array([recordio]*5) #----Vector de registros
notes=np.array([0]*5)

#Imprimir un vector de registros
def loadrecay(recarray):
    for x in range(len(recarray)):
        recarray[x]=recordio() #Agregamos esta linea para inicializar el registro en el vector
        recarray[x].names=input("Por favor, ingrese un nombre: ")
        recarray[x].surnames=input("Por favor, ingrese un apellido: ")
        recarray[x].theorical=float(input("Por favor, ingrese la nota teórica: "))
        recarray[x].practical=int(input("Por favor, ingrese la nota práctica: "))

def disrecay(recarray):
    for j in range(len(recarray)):
        print("Nombres: ",recarray[j].names)
        print("Apellidos: ",recarray[j].surnames)
        print("Nota teórica: ",recarray[j].theorical)
        print("Nota práctica: ",recarray[j].practical)

#loadrecay(recarray)
#disrecay(recarray)


