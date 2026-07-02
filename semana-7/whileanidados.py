n = 1

print("Entra al ciclo while principal")

while n < 4:
    print("numero de iteracion del ciclo while principal", n)
    i = 1
    print("Entra al ciclo while interno")
    
    while i < 6:
        print("i:", i)
        i += 1
    n = n+1

print("Fin de ciclo principal")