# Calcular año bisisesto
# si año es divisible entre 4 y no es divisible entre 100
# si año es divisible entre 100 y 400

año = int(input("Año: "))

if año >= 1582:
    if ((año % 4) == 0 and (año % 100) != 0) or ((año % 100) == 0 and (año % 400) == 0):
        print("Año Bisiesto")
    else:
        print("Año común") 
else:
    print("No dentro del período del calendario gregoriano")