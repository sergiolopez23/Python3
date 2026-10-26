num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
if num2 != 0:
    print(f"División: {num1 / num2}")
else:
    print("No se puede dividir entre cero.")
