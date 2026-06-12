# Objetivo: Toma elementos de una lista en un intervalo dado [a,b]
# tomaintervalo([1,2,3,4], 0, 3)

def tomaintervalo(lista, a, b):
    l = []
    contador = 0
    for i in lista:
        if contador >= a and contador <= b:
            l = l + [i]
        contador += 1
    return l

print(tomaintervalo([1,2,3,4,5], 3,4))