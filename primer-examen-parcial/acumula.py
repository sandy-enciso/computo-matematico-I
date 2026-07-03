# Mediante la estructura de control 'for' implemente la función acumula
# que regresa la suma de los elementos anteriores de una lista.

def first(lista):
    return lista[0]

def rest(lista):
    return lista[1:]

def acumula(lista):
    resultado = []
    a = first(lista)
    for elemento in rest(lista):
        resultado = resultado + [a]
        a = a + elemento
    resultado = resultado + [a]
    return resultado

print(acumula([7,3,1,4,6])) # ->[7,10,11,15,21]