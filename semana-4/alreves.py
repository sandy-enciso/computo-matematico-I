# Objetivo: Invertir los elementos de una lista

def alreves(lista):
    l = []
    for ele in lista:
        l = [ele] + l
    return l

print(alreves([1,2,3,4,5]))