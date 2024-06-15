## Ejercicio 3 ##


## Enunciado

# Un polinomio se puede evaluar en tiempo lineal sin necesidad de una variable auxiliar si observamos que
# P(x) se puede factorizar como: P(x) = a_0 + x(a_1 + x( ... + x(a_{n-1} + x(a_n)) ... ))
# Por ejemplo, P(x) = 5 + 2x - 3x^2 + 4x^3 = 5 + x(2 + x(-3 + x(4)))
# Programe un algoritmo iterativo que evalúe el polinomio utilizando esta idea. 
# Comience desde el paréntesis más interno y vaya avanzando hacia la izquierda. Indique cuál es el invariante que utiliza. 
# El algoritmo resultante se llama la **Regla de Horner**.

def evalp(a, x):
    """Evalúa en el punto x el polinomio cuyos coeficientes son a[0], a[1],...
    utilizando la Regla de Horner
    Retorna el valor calculado
    """
    P = 0
    for i in range(len(a) - 1, -1, -1):
        P = a[i] + x * P
    return P

print(evalp([5,2,-3,4],2))