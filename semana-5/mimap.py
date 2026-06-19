# Objetivo: Aplica la funcion a cada uno de los elementos de la lista

def mimap(funcion, lista):
    l = []
    for x in lista:
        l = l + [funcion(x)]
    return l

print(mimap(lambda x: x*x, [1, 2, 3, 4, 5]))