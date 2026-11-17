def Login(usuario, password, intentos):
  if usuario == "usuario1" and password == "asdasd":
    return True, intentos
  else:
    intentos += 1
    return False, intentos

intentos_actuales = 0
acceso_concedido = False

while intentos_actuales < 3 and not acceso_concedido:
  user = input("Usuario: ")
  passw = input("Contraseña: ")

  acceso_concedido, intentos_actuales = login(user, password, intentos_actuales)

  if acceso_concedido:
    print("Login correcto, has accedido al sistema")
  else:
    intentos_restantes = 3 - intentos_actuales
    if intentos_restantes > 0:
      print(f"Credenciales incorrectas. Te quedan {intentos_restantes} intento(s)")
    else:
      print("Has agotado los 3 intentos. Acceso bloqueado")
