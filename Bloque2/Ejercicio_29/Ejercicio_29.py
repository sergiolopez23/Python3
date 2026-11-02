base = float(input("Introduce la base (número real): "))
exponente = int(input("Introduce el exponente (entero no negativo): "))

resultado = 1.0
for _ in range(exponente):
    resultado *= base

print(f"El resultado de {base}^{exponente} es: {resultado}")
