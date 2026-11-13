def contar_caracteres(cadena):
    diccionario_frecuencia = {}
    
    for caracter in cadena:
        diccionario_frecuencia[caracter] = diccionario_frecuencia.get(caracter, 0) + 1
        
    return diccionario_frecuencia

texto = input("Introduce una cadena de texto: ")
resultado = contar_caracteres(texto)
print("Resultado:", resultado)
