# paso 1
beatles = []
print("Paso 1:", beatles)

# paso 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)

# paso 3
for i in range(2):
    beatles.append(input("Integrante: "))

print("Paso 3:", beatles)

# etapa 4
del beatles[-1]
del beatles[-1]
print("Paso 4:", beatles)

# paso 5
beatles.insert(0, "Ringo Starr")
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fab", len(beatles))
