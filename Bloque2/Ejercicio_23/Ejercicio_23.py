suma = 0
contador = 0

while True:
  num = float(input("Introduce un numero: "))
  if num == 0:
    break
  suma += num
  contador += 1

if contador > 0:
  media = suma / contador
  print("Suma total: {suma}")
  print("Media de los numeros: {media}")
else:
  print("No has introducido ningun numero distinto de cero")
