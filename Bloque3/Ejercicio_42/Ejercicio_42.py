cadena = input("Introduce la cadena principal: ")
subcadena = input("Introduce la subcadena a comprobar: ")

if cadena.startswith(subcadena):
    print(f"Sí, la cadena comienza por '{subcadena}'.")
else:
    print(f"No, la cadena NO comienza por '{subcadena}'.")
