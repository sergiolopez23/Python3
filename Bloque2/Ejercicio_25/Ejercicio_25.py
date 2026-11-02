while True:
    caracter = input("Introduce un carácter (espacio para terminar): ")
    
    if caracter == " ":
        break
    
    if len(caracter) == 1 and caracter.lower() in "aeiouáéíóú":
        print("VOCAL")
    else:
        print("NO VOCAL")
