def a_segundos(horas, minutos, segundos):
    return (horas * 3600) + (minutos * 60) + segundos

def a_hms(segundos_totales):
    horas = segundos_totales // 3600
    resto = segundos_totales % 3600
    minutos = resto // 60
    segundos = resto % 60
    return horas, minutos, segundos

while True:
    print("\n--- MENÚ DE CONVERSIÓN DE TIEMPO ---")
    print("1. Convertir a segundos")
    print("2. Convertir a horas, minutos y segundos")
    print("3. Salir")
    
    opcion = input("Elige una opción (1-3): ")
    
    if opcion == "1":
        h = int(input("Introduce las horas: "))
        m = int(input("Introduce los minutos: "))
        s = int(input("Introduce los segundos: "))
        total = a_segundos(h, m, s)
        print(f"Resultado: {total} segundos.")
        
    elif opcion == "2":
        seg = int(input("Introduce la cantidad total de segundos: "))
        h, m, s = a_hms(seg)
        print(f"Resultado: {h} hora(s), {m} minuto(s) y {s} segundo(s).")
        
    elif opcion == "3":
        print("Saliendo del programa...")
        break
        
    else:
        print("Opción no válida. Por favor, elige 1, 2 o 3.")
