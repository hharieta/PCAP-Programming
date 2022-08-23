# Laboratorio 1 del módulo 3.1.1
# un programa loco por el espatifilo

planta = input("Ingresa el nombre de una planta: ")

if planta == "Espatifilo":
    print("Si, ¡El Espatifilo es la mejor planta de todos los tiempos!")
elif planta == "espatifilo":
    print("No, ¡quiero un gran Espatifilo!")
else:
    print("¡Espatifilo! ¡No {}!".format(planta))

