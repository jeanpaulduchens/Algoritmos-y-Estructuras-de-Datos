## Ejercicio 6 ##


# Enunciado

# Una función recursiva que genera e imprime todos los números binarios de n dígitos se puede plantear 
# con un encabezado de la siguiente manera: def genera_binarios(a,k,n):
# Donde a es un arreglo que contiene los unos y ceros de los números que se van generando, 
# el cual se va rellenando con valores de izquierda a derecha, k es el grado de avance en el proceso de generación 
# (más precisamente cuantos dígitos se han generado hasta esta llamada) y 
# n es la cantidad total de dígitos que deben generarse (n = len(a)). 
# Por lo tanto n-k es la cantidad de dígitos que faltan por generar. 
# Esta función se llama la primera vez de la siguiente manera:

# import numpy as np
# n = 4
# a = np.empty(n,dtype=int) # arreglo de largo n sin inicializar
# genera_binarios(a,0,len(a))

# Se le pide que escriba las instrucciones de la función genera_binarios de acuerdo al siguiente algoritmo:
# si el valor de k es igual a n, ya se han generado todos los dígitos por lo cual se imprime el arreglo en pantalla (print(a))
# si no, se hacen dos cosas:
#  se pone un 0 en la k-ésima posicion y se llama recursivamente a la función para que genere los dígitos restantes
#  luego se pone un 1 en la misma k-ésima posición (reemplazando el 0) y se llama recursivamente a la función para que genere los dígitos restantes
# Pruebe su función con para el caso n=4. 

def genera_binarios(a, k, n):
    if k == n:
        print(a)
    else:
        a[k] = 0
        genera_binarios(a, k + 1, n)
        a[k] = 1
        genera_binarios(a, k + 1, n)

import numpy as np
n = 4
a = np.empty(n,dtype=int)
genera_binarios(a,0,len(a))