#Objetivo: Sumas los elementos de una lista

def sumalista(lista):
    resultado = 0
    while lista != []:
        resultado = resultado + lista[0]
        lista = lista[1:]
    return resultado


print(sumalista([1,2,3,4,5])) # 15
print(sumalista([])) # 0