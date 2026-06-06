#Ejemplos de estructura de control if

# Variante 1

print('Variante 1')

edad = 13

if edad < 0:
    print("Edad no valida")

if edad >= 0 and edad < 7:
    print("Eres un infante")

if edad > 6 and edad < 13:
    print("Eres un niño")

if edad > 12 and edad < 21:
    print("Eres un adolescente")

if edad > 20 and edad < 25:
    print("Eres un joven")



# Variante 2

print('Variante 2')

if edad > 17:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

a = 1
b = 3

if a > b:
    print('el mayor es', a)
else:
    print('el mayor es', b)

numero = 10

if numero > 0:
    print(numero, "es positivo")
else:
    print(numero, "es negativo")

calificacion = 8

if calificacion > 5:
    print("Aprobado")
else:
    print("Reprobado")

es_de_dia = True

if es_de_dia:
    print('Buenos días')
else:
    print('Buenas tardes')




# Variante 3

if edad < 0:
    print("Edad no valida")
elif edad >= 0 and edad < 7:
    print("Eres un infante")
elif edad > 6 and edad < 13:
    print("Eres un niño")
elif edad > 12 and edad < 21:
    print("Eres un adolescente")
elif edad > 20 and edad < 25:
    print("Eres un joven")
else:
    print("Eres un adulto")


a = 1
b = 2
c = 3

if a > b and a > c:
    print('el mayor es', a)
elif b > a and b > c:
    print('el mayor es', b)
elif c > a and c > b:
    print('el mayor es', c)
else:
    print('hay numeros iguales')


if numero == 0:
    print(numero, "es cero")
elif numero > 0:
    print(numero, "es positivo")
else:
    print(numero, "es negativo")


if calificacion < 6:
    print("Reprobado")
elif calificacion == 6:
    print('Calificacion minima aprobatoria')
elif calificacion > 6 and calificacion < 9:
    print("Aprobado")
else:
    print("Excelente")

hora = 6

if hora >= 6 and hora < 12:
    print('Buenos días')
elif hora >= 12 and hora < 20:
    print('Buenas tardes')
else:    
    print('Buenas noches')




# Variante 4

print('Variante 4')

edad = 13

if edad < 0:
    print("Edad no valida")
else:
    if edad >= 0 and edad < 7:
        print("Eres un infante")
    elif edad > 6 and edad < 13:
        print("Eres un niño")
    elif edad > 12 and edad < 21:
        print("Eres un adolescente")
    elif edad > 20 and edad < 25:
        print("Eres un joven")
    else:
        print("Eres un adulto")


if a <= 0 or b <= 0 or c <= 0:
    print('Ingresa numeros positivos')
else:
    if a > b and a > c:
        print('el mayor es', a)
    elif b > a and b > c:
        print('el mayor es', b)
    elif c > a and c > b:
        print('el mayor es', c)
    else:
        print('hay numeros iguales')
    

if numero == 0:
    print('es cero')
else:
    if numero > 0:
        print(numero, "es positivo")
    else:
        print(numero, "es negativo")


if calificacion < 0 or calificacion > 10:
    print("Calificacion no valida")
else:
    if calificacion < 6:
        print("Reprobado")
    elif calificacion == 6:
        print('Calificacion minima aprobatoria')
    elif calificacion > 6 and calificacion < 9:
        print("Aprobado")
    else:
        print("Excelente")


if hora < 0 or hora > 23:
    print('Hora no valida')
else:
    if hora >= 6 and hora < 12:
        print('Buenos días')
    elif hora >= 12 and hora < 20:
        print('Buenas tardes')
    else:    
        print('Buenas noches')