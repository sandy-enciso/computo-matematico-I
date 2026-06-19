# Objetivo: Regresa el numero mayor de una lista de numeros

def maximo(lista):
    elemento = lista[0]
    for i in lista:
        if i > elemento:
            elemento = i
    return elemento

print(maximo([7,6,23,10])) # -> 23