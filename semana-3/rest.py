# Programa: rest
# Objetivo: Regresar el resto de los elementos de una lista (excluye el primer elemento)
# rest: lista -> lista
# rest(lista) -> lista

def rest(lista): return lista[1:]

print(rest([7,8,6,5]))
print(rest(['jose','maria','guadalupe']))
print(rest([3.14,False,65,'a']))