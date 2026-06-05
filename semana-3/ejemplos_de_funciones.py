#Conversion de tipos}

int("32") # Convierte un string a tipo entero

str(32) # Convierte un entero a string

int(3.9999) # Convierte float a entero

float(3) # Convierte un entero a float

#Coercion de tipos

minutos = 59
minutos/60 # Solo retorna la parte entera

float(minutos)/60 # Retorna float

minutos/60.0 # Retorna float

import math # Para importar la libreria de funciones matematicas

math.sin(1.5)

math.cos(2.0)

math.tan(2.1)

math.pi

grados = 45

angulo = grados * 2 * (math.pi/360.0)

math.sin(angulo)

math.cos(45 + math.pi/2)

math.cos(math.sin(1.5))

