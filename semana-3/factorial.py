# Factorial

def crea_intervalo_aux(a,b,l):
    if a > b:
        return l
    else:
        return crea_intervalo_aux(a+1, b, l+[a])
    
def crea_intervalo(a,b): return crea_intervalo_aux(a,b,[])

print(crea_intervalo(1,10))

def factorial(n):
    f = 1
    for i in crea_intervalo(1,n):
        f *= i
    return f

print(factorial(5))