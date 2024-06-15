## Ejercicio 5 ##

## Enunciado

# Una función recursiva que genera e imprime todas las permutaciones de un arreglo se puede plantear de la siguiente manera:
# def permutaciones(x,ini,fin):
# genera las permutaciones del arreglo x desde el elemento con índice ini hasta el elemento con índice fin
# Si  𝑖𝑛𝑖  es igual a  𝑓𝑖𝑛  implica que se pide la permutación de un solo elemento, y en ese momento se imprime todo el contenido del arreglo
# De lo contrario, para todos los elementos  𝑥[𝑖]  con  𝑖  desde  𝑖𝑛𝑖  hasta  𝑓𝑖𝑛  ( 𝑓𝑖𝑛  incluido) se hace lo siguiente:
           # . se intercambia el valor del i-ésimo elemento con el inicial
           # . se llama recursivamente a la función permutaciones con el 
              # índice del primer elemento incrementado: permutaciones(x, ini+1, fin)
           # . Se vuelven a restaurar los valores del elemento inicial con el i-ésimo
# Implemente la función "permutaciones" que imprima todas las permutaciones de un arreglo de entrada. Probar su función con arreglos de tamaño 1, 3 y 5.

def permutaciones(x, ini, fin):
    if ini == fin:
        print(x)
    else:
        for i in range(ini, fin + 1):
            x[ini], x[i] = x[i], x[ini]  # Intercambia el elemento inicial con el i-ésimo elemento
            permutaciones(x, ini + 1, fin)  # Llama recursivamente con el siguiente elemento inicial
            x[ini], x[i] = x[i], x[ini]  # Restaura el intercambio

# Prueba de la función con arreglos de tamaño 1, 3 y 5
print("Permutaciones de [1]:")
permutaciones([1], 0, 0)

print("\nPermutaciones de [1, 2, 3]:")
permutaciones([1, 2, 3], 0, 2)

print("\nPermutaciones de [1, 2, 3, 4, 5]:")
permutaciones([1, 2, 3, 4, 5], 0, 4)
