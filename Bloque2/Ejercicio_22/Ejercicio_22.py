numero = random.randint(1,100)
intentos_restantes = 10
acertado = False

print("Aivina el numero del 1 al 100")

for intento in range(1,11):
  print(f"Te quedan {intentos_restantes} intentos")
  num = int(input(Introduce un numero: ))

  if num == numero_secreto:
    print(f"Muy bien, has acertado el numero en {intento} intentos")
    acertado = True
    break
  elif num < numero:
    print("El numero a adivinar es mayor")
  else:
    print("El numero a adivinar es menor")

  intentos_restantes -= 1

if not acertado:
  print(f"Has gastado todos tus intentos El número secreto era: {numero}")
  
