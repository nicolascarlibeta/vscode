# Array - Vector o Arreglo
# Es una estructura de datos con las siguientes características:
#    Homogeneo: Todo los elementos del vector son del mismo tipo.
#    Indizado : Tiene un indice por el cual se puede acceder a los elementos del vector.
#    Estático : No cambia la cantidad de elementos una vez definido.

import os # para saber sobre que sistema operativo se está ejecutando el programa.

def limpiar_pantalla():
#  Esto sirve para detectar el Sist Operativo
#  Y envía la orden de limpiar la pantalla según corresponda.
#  'posix' (sistemas POSIX y distribuciones de Linux).
#  'nt' (Windows).
    if (os.name)=='posix':
        os.system('clear')
    if (os.name)=='nt':
        os.system('cls')

def cargarv(v,c):
    for i in range(c):
        v[i]=int(input("Ingrese la Nota: "))

def mostrarv(v,c):
    for i in range(c):
        print(vec1[i], end="   ")

def prom(v,c): # Calcula y retorna el promedio.
    suma=0
    for i in range(c):
        suma = suma+vec1[i]
    pro=suma/cant
    return pro
            
def pres_enter(): # Pone el cartel de presione Enter para continuar y limpia la pantalla.
    print()
    input("Presione Enter para continuar...")
    limpiar_pantalla()

def cant_alu(): # Solicita la cantidad de notas y las retorna.
    cantidad=int(input("Ingrese la Cantidad de Alumnos a cargar: "))
    return cantidad

# Programa Principal

limpiar_pantalla()
cant=cant_alu()   # Se ingresa por teclado la cantidad de notas a cargar
# Definir el vector
vec1=[0]*cant   # Se define el tamaño del vector usando la cantidad de notas

limpiar_pantalla() # Limpio la pantalla antes de mostrar el menú
# Menú
op=100 # Instancio la variable op con un valor distinto de 0 (cero) para que ingrese al while
while op!=0:
    print("      Menú")
    print()
    print("  1 Cargar Notas")
    print("  2 Mostrar notas")
    print("  3 Ver promedio")
    print("  0 Salir")
    print()
    op=int(input(" Elija una opción: "))

    if op==1:
        cargarv(vec1,cant)
        pres_enter()
    elif op==2:
        mostrarv(vec1,cant)
        pres_enter()
    elif op==3:
        print(f'El promedio de las notas es: {prom(vec1,cant)}')
        pres_enter()
    elif op==0:
        print("Hasta la próxima")
        pres_enter()
    else:
        print("Opción Incorrecta")
        pres_enter()
