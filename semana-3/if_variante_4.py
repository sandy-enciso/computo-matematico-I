# if predicado1:
#     sentencia1
#     ...
#     sentencian
# else:
#     if predicado2:
#         sentencia1
#         ...
#         sentencian
#     else:
#         if predicado3:
#             sentencia1

x=100
y=200

if x==y:
    print(x,'y',y, 'son iguales')
else:
    if x < y:
        print(x, 'es menor que', y)
    else:
        print(x,'es mayor que', y)
