# programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares
# programa termina cuando se ingresa cero

numerosImpares = 0
numerosPares = 0

# lee el primer número
numero = int (input ("Introduce un número o escriba 0 para detener:"))

# dado que la experesión while toma la condicionante numero como booleano
# un 0 termina la ejecución del ciclo, puesto que 0 = False
# print("False vale: ", int(False)) # 0
# print("True vale: ", int(True)) # 1
while numero:
    # verificar si el número es impar
    if numero % 2 == 1: numerosImpares += 1
    else: numerosPares += 1
    # lee el siguiente número
    numero = int (input ("Introduce un número o escriba 0 para detener:"))

# imprimir resultados
print("Números impares: ", numerosImpares)
print("Números pares: ", numerosPares)