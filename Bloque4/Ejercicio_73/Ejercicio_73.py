agenda = {}

while True:
    print("\n--- AGENDA TELEFÓNICA ---")
    print("1. Añadir / Modificar contacto")
    print("2. Buscar contacto")
    print("3. Borrar contacto")
    print("4. Listar todos los contactos")
    print("5. Salir")
    
    opcion = input("\nElige una opción (1-5): ")
    
    if opcion == "1":
        nombre = input("Introduce el nombre del contacto: ").strip()
        if nombre in agenda:
            print(f"El contacto '{nombre}' ya existe. Teléfono actual: {agenda[nombre]}")
            modificar = input("¿Deseas modificar el teléfono? (s/n): ").lower()
            if modificar == "s":
                nuevo_tel = input("Introduce el nuevo teléfono: ").strip()
                agenda[nombre] = nuevo_tel
                print("Teléfono actualizado correctamente.")
        else:
            telefono = input("Introduce el teléfono: ").strip()
            agenda[nombre] = telefono
            print(f"Contacto '{nombre}' añadido a la agenda.")
            
    elif opcion == "2":
        cadena = input("Introduce el inicio del nombre a buscar: ").strip().lower()
        encontrados = False
        print("\nResultados de la búsqueda:")
        for nombre, telefono in agenda.items():
            if nombre.lower().startswith(cadena):
                print(f"  - {nombre}: {telefono}")
                encontrados = True
        if not encontrados:
            print("  No se encontraron contactos que empiecen por esa cadena.")
            
    elif opcion == "3":
        nombre = input("Introduce el nombre del contacto a borrar: ").strip()
        if nombre in agenda:
            confirmar = input(f"¿Seguro que quieres borrar a '{nombre}' ({agenda[nombre]})? (s/n): ").lower()
            if confirmar == "s":
                del agenda[nombre]
                print("Contacto eliminado.")
            else:
                print("Operación cancelada.")
        else:
            print(f"El contacto '{nombre}' no existe en la agenda.")
            
    elif opcion == "4":
        if not agenda:
            print("La agenda está vacía.")
        else:
            print("\n--- LISTA DE CONTACTOS ---")
            for nombre, telefono in agenda.items():
                print(f"  - {nombre}: {telefono}")
                
    elif opcion == "5":
        print("Saliendo de la agenda...")
        break
        
    else:
        print("Opción no válida. Por favor, elige un número del 1 al 5.")
