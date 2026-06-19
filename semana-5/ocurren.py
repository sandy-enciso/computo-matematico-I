# Objetivo: Determina las veces que ocurren los elementos de una lista en otra lista.

def ocurren(lista1, lista2):
    resultado = []
    for i in lista1:
        contador = 0
        for j in lista2:
            if i == j:
                contador += 1
        resultado = resultado + [contador]
    return resultado

print(ocurren([1,2], [1,2,1,2,1])) # -> [3, 2]