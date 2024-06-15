## Ejercicio 4 ##


## Enunciado 

# Se le llama "Camel Case" a la convención de escribir una frase sin espacios, 
# pero marcando el inicio de cada palabra poniendo su primera letra en mayúscula. 
# Por ejemplo, la frase: "  Algoritmos y    estructuras de   datos   "
# transformada a Camel Case queda así: "AlgoritmosYEstructurasDeDatos"
# Escriba una función que transforme a Camel Case y pruébela:

def CamelCase(s):
    """Retorna un string conteniendo la versión Camel Case del string s"""
    camel_case = ""
    capitalize_next = True

    for char in s:
        if char == " ":
            capitalize_next = True
        else:
            if capitalize_next:
                camel_case += char.upper()
                capitalize_next = False
            else:
                camel_case += char.lower()

    return camel_case

print(CamelCase("    Algoritmos y    estructuras de   datos   "))