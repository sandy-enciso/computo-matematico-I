# Ojetivo: Calcular la potencia de un numero

def crea_lista_aux(n,cuenta,l):
    if n == 0:
        return l
    else:
        return crea_lista_aux(n-1, cuenta+1, l+[cuenta])
    
def crea_lista(a): return crea_lista_aux(a,0,[])

print(crea_lista(3))

def potencia(b,n):
    if b == 0: return False
    p = 1
    for i in crea_lista(n):
        p *= b
    return p

print(potencia(2,3))