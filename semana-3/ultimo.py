# objetivo: regresa el ultimo elemento de una lista

def first(lista):
    return lista[0]

def ultimo(lista):
    l = []
    for elemento in lista:
        l = [elemento] + l
    return first(l)

print(ultimo([8,6,4,3]))