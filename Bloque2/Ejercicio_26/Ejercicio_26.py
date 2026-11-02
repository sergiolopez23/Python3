num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

inicio = min(num1, num2)
fin = max(num1, num2)

print(f"Números pares entre {inicio} y {fin}:")
for i in range(inicio, fin + 1):
    if i % 2 == 0:
        print(i, end=" ")
print()
