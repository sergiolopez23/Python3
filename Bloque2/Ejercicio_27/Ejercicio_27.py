num = int(input("Introduce un número para ver su tabla de multiplicar: "))

print(f"\n--- Tabla de multiplicar del {num} ---")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
