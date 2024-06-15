## Ejercicio 2 ## 


# Enunciado 

# Existe un algoritmo alternativo a Hoare, que resulta en una codificación más sencilla. 
# Este algoritmo, debido a Lomuto, se basa en el siguiente invariante:
# En este algoritmo, en cada iteración, si  𝑎[𝑗]<𝑝 , se intercambian  𝑎[𝑖]  con  𝑎[𝑗]  y se incrementa  𝑖 ,
#  porque ahora hay un elemento más en el grupo de los menores que  𝑝 . Después de esto, se incrementa  𝑗 incondicionalmente 
# (¿por qué es correcto hacer eso?).
# Programe la partición de Lomuto en el recuadro siguiente y pruébela.

def particionLomuto(a, p):
    i = 0
    for j in range(len(a)):
        if a[j] < p:
            a[i], a[j] = a[j], a[i]
            i += 1
    return (p, i, a)

def verifica_particion(t): # imprime y chequea partición
    (p,m,a)=t
    # p=punto de corte, m=número de elementos <p, a=lista completa particionada
    print(a[0:m],p,a[m:])
    print("Partición OK" if (m==0 or max(a[0:m])<p) and (m==len(a) or min(a[m:])>p)
          else "Error")
    
verifica_particion(particionLomuto([73,21,34,98,56,37,77,65,82,15,36],50))
verifica_particion(particionLomuto([73,21,34,98,56,37,77,65,82,15,36],0))
verifica_particion(particionLomuto([73,21,34,98,56,37,77,65,82,15,36],100))