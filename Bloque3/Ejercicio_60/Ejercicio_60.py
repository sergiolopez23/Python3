tabla = []

print("Introduce los valores enteros para la tabla de 5x5:")
for i in range(5):
    fila = []
    for j in range(5):
        while True:
            try:
                valor = int(input(f"Introduce el valor para la posición [{i}][{j}]: "))
                fila.append(valor)
                break
            except ValueError:
                print("Error: Introduce un número entero válido.")
    tabla.append(fila)

print("\n--- Tabla de 5x5 ---")
for fila in tabla:
    print("\t".join(map(str, fila)))

print("\n--- Suma de cada fila ---")
for i, fila in enumerate(tabla):
    suma_fila = sum(fila)
    print(f"Fila {i}: {suma_fila}")

print("\n--- Suma de cada columna ---")
for j in range(5):
    suma_columna = sum(tabla[i][j] for i in range(5))
    print(f"Columna {j}: {suma_columna}")
