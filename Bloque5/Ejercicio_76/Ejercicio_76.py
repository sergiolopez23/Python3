def EsMultiplo(num1, num2):
  if num2 == 0:
    return False
  return num1 % num2 == 0

numero1 = int(input("Introduce el primer numero entero: "))
numero2 = int(input("Introduce el segundo numero entero: "))

if es_multiplo(numero1, numero2):
  print(f"{numero1} es multiplo de {numero2}")
elif es_multiplo(numero2, numero1):
  print(f"{numero2} es multiplo de {numero1}")
else:
  print("Ninguno de los dos números es múltiplo del otro")
