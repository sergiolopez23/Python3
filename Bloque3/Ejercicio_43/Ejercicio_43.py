cadena = input("Introduce una cadena de texto: ")

while True:
    caracter = input("Introduce un único carácter a buscar: ")
    if len(caracter) == 1:
        break
    print("Error: Debes introducir exactamente un carácter. Inténtalo de nuevo.")

contador = cadena.count(caracter)

print(f"El carácter '{caracter}' aparece {contador} vez/veces en la cadena.")
