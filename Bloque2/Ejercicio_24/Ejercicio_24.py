cantidad = int(input("¿Cuántos números vas a introducir?: "))

mayores_cero = 0
menores_cero = 0
iguales_cero = 0

for i in range(cantidad):
    num = float(input(f"Número {i+1}: "))
    if num > 0:
        mayores_cero += 1
    elif num < 0:
        menores_cero += 1
    else:
        iguales_cero += 1

print(f"Resultados: ")
print(f"Mayores que 0: {mayores_cero}")
print(f"Menores que 0: {menores_cero}")
print(f"Iguales a 0: {iguales_cero}")
