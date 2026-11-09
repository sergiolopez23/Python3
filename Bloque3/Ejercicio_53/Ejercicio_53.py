notas = []

print("Introduce las 5 notas del alumno (valores entre 0 y 10):")
for i in range(1, 6):
    while True:
        try:
            nota = float(input(f"Nota {i}: "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("Error: La nota debe estar comprendida entre 0 y 10.")
        except ValueError:
            print("Error: Introduce un valor numérico válido.")

print("\n--- Resultados ---")
print(f"Todas las notas: {notas}")
print(f"Nota media: {sum(notas) / len(notas):.2f}")
print(f"Nota más alta: {max(notas)}")
print(f"Nota más baja: {min(notas)}")
