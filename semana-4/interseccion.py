# Objetivo: Realizar la interseccion de dos conjuntos
# interseccion([1,2,3,4], [3,4,5,6]) -> [3,4]

def interseccion(lista1, lista2):
    l = []
    for i in lista1:
        if i in lista1 and i in lista2:
            l = l + [i]
    return l

print(interseccion([1,2,3,4], [3,4,5,6]))