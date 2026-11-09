nombre_completo = input("Introduce tu nombre y apellidos: ")

palabras = nombre_completo.split()
iniciales = ""

for palabra in palabras:
    iniciales += palabra[0].upper()

print(f"Las iniciales son: {iniciales}")
