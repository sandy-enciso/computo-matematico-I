# Objetivo: Realiza la union entre dos conjuntos
# union([1,2,3,4,5], [3,4,5,6,7,8]) -> [1,2,3,4,5,6,7,8]

def union(lista1, lista2):
    l = []
    for i in lista1:
        if i not in l:
            l = l + [i]
    for i in lista2:
        if i not in l:
            l = l + [i]
    return l

print(union([1,2,3,4,5], [3,4,5,6,7,8]))

print(union([1,2,3,4], []))

print(union([1,2,3,4], [1,2,3,4]))