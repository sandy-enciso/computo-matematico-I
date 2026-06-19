# Objetivo: Filtrar una lista a partir de una funcion predicado

def selecciona(lista, predicado):
    l = []
    for i in lista:
        if predicado(i):
            l = l + [i]
    return l


print(selecciona([1,2,3,4,5,6], lambda x: x % 2 == 0)) # [2,4,6]