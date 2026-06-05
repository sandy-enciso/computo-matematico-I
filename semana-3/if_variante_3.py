# if predicado1:
#     sentencia1
#     sentencia2
#     ...
#     sentencian
# elif predicado2:
#     sentencia1
#     sentencia2
#     ...
#     sentencian
# elif:
#     ...
# else:
#     sentencia

x=5
y=6

if x<y:
    print(x, "es menor que", y)
elif x>y:
    print(x,"es mayor que", y)
else:
    print(x, "y", y, "son iguales")

eleccion='A'

if eleccion=='A':
    print('elegiste la opcion A')
elif eleccion=='B':
    print('elegiste B')
elif eleccion=='C':
    print('elegiste C')
else:
    print('eleccion no valida')
