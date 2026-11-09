meses = [
    "Enero", "Febrero", "Marzo", "Abril", 
    "Mayo", "Junio", "Julio", "Agosto", 
    "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

try:
    numero_mes = int(input("Introduce el número de mes (1-12): "))
    
    if 1 <= numero_mes <= 12:
        indice = numero_mes - 1
        nombre_mes = meses[indice]
        total_dias = dias[indice]
        
        print(f"El mes {numero_mes} es **{nombre_mes}** y tiene **{total_dias} días**.")
    else:
        print("Error: El número debe estar comprendido entre 1 y 12.")
        
except ValueError:
    print("Error: Debes introducir un valor numérico entero.")
