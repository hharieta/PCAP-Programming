num1 = int(input("número 1: "))
num2 = int(input("número 2: "))
num3 = int(input("número 3: "))

mayor = num1

if num2 > mayor: mayor = num2
if num3 > mayor: mayor = num3

print("el mayor es: ", mayor)
