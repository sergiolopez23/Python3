while True:
    limite_inferior = float(input("Introduce el límite inferior: "))
    limite_superior = float(input("Introduce el límite superior: "))
    
    if limite_inferior <= limite_superior:
        break
    print("Error: El límite inferior debe ser menor o igual que el límite superior. Inténtalo de nuevo.\n")

suma_dentro = 0
fuera_intervalo = 0
igual_a_limite = False

print("\nIntroduce números (introduce 0 para salir):")
while True:
    num = float(input("Número: "))
    if num == 0:
        break
    
    if limite_inferior < num < limite_superior:
        suma_dentro += num
    else:
        fuera_intervalo += 1
        
    if num == limite_inferior or num == limite_superior:
        igual_a_limite = True

print(f"\nSuma de los números dentro del intervalo abierto ({limite_inferior}, {limite_superior}): {suma_dentro}")
print(f"Cantidad de números fuera del intervalo: {fuera_intervalo}")
if igual_a_limite:
    print("Se introdujo al menos un número igual a uno de los límites.")
else:
    print("No se introdujo ningún número igual a los límites.")
