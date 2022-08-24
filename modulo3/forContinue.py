palabra = input("Palabra: ")

for letra in palabra.upper():
    if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
        continue
    print(letra)

