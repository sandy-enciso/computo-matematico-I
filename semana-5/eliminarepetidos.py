# Elimina los elementos repetidos de una lista

def eliminar_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l = l + [i]
    return l

print(eliminar_repetidos([1,3,2,1,2,3,4,5,1])) # -> [1, 3, 2, 4, 5]
print(eliminar_repetidos([1,1,1,1,1,1])) # -> [1]