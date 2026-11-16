lista = []

while True:
    print("\n--- MENÚ DE GESTIÓN DE LISTA ---")
    print("1. Añadir número a la lista")
    print("2. Añadir número en una posición")
    print("3. Longitud de la lista")
    print("4. Eliminar el último número")
    print("5. Eliminar un número por posición")
    print("6. Contar apariciones de un número")
    print("7. Posiciones de un número")
    print("8. Mostrar números")
    print("9. Salir")
    
    opcion = input("\nElige una opción (1-9): ")
    
    if opcion == "1":
        num = int(input("Introduce el número a añadir: "))
        lista.append(num)
        print(f"Número {num} añadido al final.")
        
    elif opcion == "2":
        num = int(input("Introduce el número a añadir: "))
        pos = int(input("Introduce la posición (empezando en 1): "))
        if 1 <= pos <= len(lista):
            lista.insert(pos - 1, num)
            print(f"Número {num} insertado en la posición {pos}.")
        else:
            print(f"Error: La posición {pos} no existe (rango válido: 1 a {len(lista)}).")
            
    elif opcion == "3":
        print(f"Longitud actual de la lista: {len(lista)} elemento(s).")
        
    elif opcion == "4":
        if len(lista) > 0:
            eliminado = lista.pop()
            print(f"Se ha eliminado el último número: {eliminado}")
        else:
            print("La lista está vacía, no hay nada que eliminar.")
            
    elif opcion == "5":
        pos = int(input("Introduce la posición a eliminar (empezando en 1): "))
        if 1 <= pos <= len(lista):
            eliminado = lista.pop(pos - 1)
            print(f"Se ha eliminado el número {eliminado} de la posición {pos}.")
        else:
            print(f"Error: La posición {pos} no existe en la lista.")
            
    elif opcion == "6":
        num = int(input("Introduce el número a contar: "))
        apariciones = lista.count(num)
        print(f"El número {num} aparece {apariciones} vez/veces en la lista.")
        
    elif opcion == "7":
        num = int(input("Introduce el número a buscar: "))
        posiciones = [i + 1 for i, valor in enumerate(lista) if valor == num]
        if posiciones:
            print(f"El número {num} está en las posiciones: {posiciones}")
        else:
            print(f"El número {num} no se encuentra en la lista.")
            
    elif opcion == "8":
        print("Contenido de la lista:", lista)
        
    elif opcion == "9":
        print("Saliendo del programa...")
        break
        
    else:
        print("Opción no válida. Elige un número del 1 al 9.")
