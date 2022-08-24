bloques = int(input("Cantidad de bloques: "))
altura = 1

bloquesActuales = (bloques-1)

for bloque in range(bloques):

    if bloquesActuales > (altura):
        bloquesActuales -= (altura+1)
        altura += 1
        # print("bloques actuales: ", bloquesActuales)
        # print("altura: ", altura)
    else:
        break

print("La altura de la pirámide:", altura)
