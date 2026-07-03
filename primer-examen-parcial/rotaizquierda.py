# Mediante la estructura For implemente la funcion rotaIzquierda que rota (mueve)
# los 'n' primeros elementos al final de la lista

def first(lista):
    return lista[0]

def rest(lista):
    return lista[1:]

def crea_lista(inicio, fin):
    if inicio >= fin:
        return []
    
    return [inicio] + crea_lista(inicio+1, fin)

def longitud(lista):
    longitud = 0
    for _ in lista:
        longitud += 1
    return longitud

def rotaizquierda(lista, n):
    if n == 0: return lista
    if lista == []: return []

    long = longitud(lista)
    
    n = n % long

    if n == 0:
        return lista
    
    resultado = lista

    for _ in crea_lista(0,n):
        resultado = rest(resultado) + [first(resultado)]
    return resultado



print(rotaizquierda([1,4,2,3],0)) # -> [1,4,2,3]
print(rotaizquierda([1,4,2,3],1)) # -> [4,2,3,1]
print(rotaizquierda([1,4,2,3],2)) # -> [2,3,1,4]
print(rotaizquierda([1,4,2,3],3)) # -> [3,1,4,2]
print(rotaizquierda([1,4,2,3],4)) # -> [1,4,2,3]
print(rotaizquierda([1,4,2,3],5)) # -> [4,2,3,1]