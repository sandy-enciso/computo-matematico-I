# Cuenta los elementos contiguos que hay en una lista dada
# Utilizando for

def first(lista):
    return lista[0]

def rest(lista):
    return lista[1:]

def cuentagrupos(lista):
    if lista == []: return []
    
    resultado = []
    n = first(lista)
    i = 1
    for elemento in rest(lista):
        if n == elemento:
            i += 1
        else:
            resultado = resultado + [i]
            i = 1
        n = elemento

    resultado = resultado + [i]
    return resultado


print(cuentagrupos([1, 2, 1, 1, 1, 2, 1, 1, 2, 2, 2, 1])) # -> [1,1,3,1,2,3,1]
print(cuentagrupos([1, 2, 1, 1, 1, 2, 2, 1, 1, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2])) # -> [1, 1, 3, 2, 2, 4, 4, 2]
print(cuentagrupos([1, 2, 3, 4, 5, 6, 7, 8])) # -> [1, 1, 1, 1, 1, 1, 1, 1]
print(cuentagrupos([1, 1, 2, 3, 4, 5, 6, 6, 6, 7, 8, 8])) # -> [2, 1, 1, 1, 1, 3, 1, 2]
print(cuentagrupos([])) # -> []
print(cuentagrupos([1])) # -> [1]
print(cuentagrupos([1, 1])) # -> [2]