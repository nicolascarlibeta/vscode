


#Trabajo Práctico 1

import random

#1)

array=[0]*20
array2=[0]*20

#Producto Escalar: Sigma a(x)*a2(x)

contador=0
while contador!=50:
    for x in range(20):
        contador=contador+1
        array[x]=random.randint(1,12)
        array2[x]=random.randint(1,12)