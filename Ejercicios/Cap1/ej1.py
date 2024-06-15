## Ejercicio 1 ##


## Enunciado

#La función maximo() hace n-1 comparaciones de elementos para encontrar el máximo de un conjunto de tamaño n.

# Encuentra el máximo de una lista a
def maximo(a):
    m=a[0]
    # Al comenzar cada iteración, se cumple que m==max(a[0],...,a[k-1])
    for k in range(1,len(a)):
        if a[k]>m:
            m=a[k]
    return m

print(maximo([25, 42, 93, 17, 54, 28]))

## Parte a)

# Supongamos que se desea escribir una función minmax() que al ser llamada con una lista de números, 
# retorne un par ordenado/tupla (min,max), con el mínimo y el máximo elemento del conjunto, respectivamente. 
# Escriba a continuación esa función haciendo dos pasadas sobre los datos: 
# una para encontrar el mínimo y otra para encontrar el máximo, y pruébela sobre una lista de ejemplo.

# Encuentra el máximo de una lista a
def maximo(a):
    m = a[0]
    for k in range(1, len(a)):
        if a[k] > m:
            m = a[k]
    return m

# Encuentra el mínimo de una lista a
def minimo(a):
    m = a[0]
    for k in range(1, len(a)):
        if a[k] < m:
            m = a[k]
    return m

# Encuentra el mínimo y el máximo de una lista a
def minmax(a):
    min_element = minimo(a)
    max_element = maximo(a)
    return (min_element, max_element)

# Probar la función con una lista de ejemplo
print(minmax([25, 42, 93, 17, 54, 28]))


## Parte b)

# La función anterior debería hacer  2𝑛−2  comparaciones de elementos 
# ( 2𝑛−3  si se evita comparar el elemento seleccionado en la primera pasada). 
# ¿Será posible encontrar el mínimo y el máximo haciendo muchas menos comparaciones?

# ¡La respuesta es que sí! Veámoslo con un ejemplo. Para simplificar, supongamos que la lista es de largo par:
# [45,21,34,67,55,89,44,12] 
# Luego comparemos cada elemento que está en una posición par con su vecino de la derecha, 
# e intercambiémoslos de modo que el par quede en orden ascendente (recuerde que las posiciones comienzan desde cero):
# [21,45,34,67,55,89,12,44] 
# Luego hagamos una pasada solo sobre las posiciones pares para encontrar el mínimo ( 12 ), 
# y otra pasada solo entre las posiciones impares para encontrar el máximo ( 89 ). ¡Listo!
# Programe este nuevo algoritmo, pruébelo y diga cuántas comparaciones hace en total:

def minmax_2(a):
    # Lista tiene largo par
    if len(a) % 2 != 0:
        raise ValueError("La lista debe tener un largo par")
    
    n = len(a)
    
    # Comparar cada par de elementos y ordenar
    for i in range(0, n, 2):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
    
    # Encontrar el mínimo en posiciones pares
    min_element = a[0]
    for i in range(2, n, 2):
        if a[i] < min_element:
            min_element = a[i]
    
    # Encontrar el máximo en posiciones impares
    max_element = a[1]
    for i in range(3, n, 2):
        if a[i] > max_element:
            max_element = a[i]
    
    return (min_element, max_element)

print(minmax_2([45, 21, 34, 67, 55, 89, 44, 12]))

# Para una lista de largo n, el número total de comparaciones será:
# n/2 comparaciones para ordenar los pares de elementos.
# n/2 - 1 comparaciones para encontrar el mínimo en las posiciones pares.
# n/2 - 1 comparaciones para encontrar el máximo en las posiciones impares.
# En total tenemos (n / 2) + (n / 2 - 1) = n - 1 comparaciones.