def EscribirCentrado(texto)
longitud = len(texto)
espacios = 40 - (longitud // 2)

if espacios < 0:
    espacios = 0

print(" " * espacios + texto)
print(" " * espacios + "=" * longitud)

mensaje = input("Escribe un mensaje para centrar: ")
EscribirCentrado(mensaje)
