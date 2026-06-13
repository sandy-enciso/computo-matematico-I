# Objetivo: Elimina un elemento de una lista (solo la primera vez que aparece)

def elimina(lista, elemento):
    l = []
    eliminado = False
    for i in lista:
        if i == elemento and not eliminado:
            eliminado = True
        else:
            l = l + [i]
    return l

print(elimina([1,2,5,3,4,5], 5))