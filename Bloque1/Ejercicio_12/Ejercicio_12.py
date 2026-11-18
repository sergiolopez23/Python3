x1 = float(input("Escribe el primer numero del primer par: "))
y1 = float(input("Escribe el segundo numero del primer par: "))
x2 = float(input("Escribe el primer numero del segundo par: "))
y2 = float(input("Escribe el segundo numero del segundo par: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"La distacia que hay entre esos numeros es de {distancia}")
