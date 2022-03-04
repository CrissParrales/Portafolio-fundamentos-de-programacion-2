#Un año es bisiesto si es divisible por 4 y no es por 100, o si es divisible por 400. 
#Escribe un programa que lea un año y devuelva si es bisiesto o no.

anho = int(input("Introduce el año:"))

if anho % 4 == 0 and anho % 100!= 0 or anho % 400 == 0:
    print(anho, "es un año bisiesto")
else:
    print(anho, "no es un anho bisiesto")
