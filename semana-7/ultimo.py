# Objetivo: Regresa el ultimo elemento de una lista

def ultimo(lista):
    while len(lista) > 1:
        lista = lista[1:]
    return lista[0]

print(ultimo([1,2,"hola",[1,2]]))