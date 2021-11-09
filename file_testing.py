

#Abrir un archivo
#Escribir un archivo
#Leer un archivo
#Agregar a un archivo
#Cerrar un archivo

#Abrir un archivo: abrir un archivo para leerlo o escribirlo

# variable=open("nombre del archivo","modo")

#Escribir un archivo: 

#Write (W): sobrescribir un archivo existente, eliminando los datos anteriores

var2="Microsoft Cinemania"

var1=open("cinemania.txt","a") #-----Abrimos el archivo

linea=var2 + '\n' #Agrega un salto de linea
for x in range(5):
    var1.write(linea)

var1.close() #----Cerramos el archivo

#Leer un archivo:

#Read (R): leer el contenido actual del archivo

var1=open("cinemania.txt","r")

linea=var1.readline().strip()
print(linea)
while linea!="":
    linea=var1.readline().strip()
    print(linea)

var1.close()

#Agregar a un archivo:

#Append (A): agregar una linea por debajo (sin modificar) de los datos existentes

var1=open("cinemania.txt","a")

linea="Microsoft Cinemania" + '\n'
for x in range(5):  #Agrego 5 lineas adicionales
    var1.write(linea)
                    
#Cerrar un archivo:

#Debemos cerrar el archivo despues de cada modo

var1.close()





