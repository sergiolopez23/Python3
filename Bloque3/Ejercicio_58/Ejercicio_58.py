alumnos = []

print("Introduce los datos de los alumnos. Escribe '*' en el nombre para finalizar.")

while True:
    nombre = input("Introduce el nombre del alumno (o '*' para terminar): ").strip()
    if nombre == '*':
        break
    
    try:
        edad = int(input(f"Introduce la edad de {nombre}: "))
        if edad < 0:
            print("Error: La edad no puede ser negativa.")
            continue
    except ValueError:
        print("Error: Introduce un valor numérico entero para la edad.")
        continue
        
    alumnos.append({"nombre": nombre, "edad": edad})

if not alumnos:
    print("\nNo se han introducido datos.")
else:
    print("\n--- Resultados ---")
    
    mayores_edad = [a for a in alumnos if a["edad"] >= 18]
    print("\nAlumnos mayores de edad:")
    if mayores_edad:
        for a in mayores_edad:
            print(f"- {a['nombre']} ({a['edad']} años)")
    else:
        print("No hay alumnos mayores de edad.")
        
    max_edad = max(a["edad"] for a in alumnos)
    alumnos_mayor_edad = [a for a in alumnos if a["edad"] == max_edad]
    
    print(f"\nAlumno(s) con mayor edad ({max_edad} años):")
    for a in alumnos_mayor_edad:
        print(f"- {a['nombre']}")
