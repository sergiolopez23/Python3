parcial1 = float(input("Introduce la nota del primer parcial: "))
parcial2 = float(input("Introduce la nota del segundo parcial: "))
parcial3 = float(input("Introduce la nota del tercer parcial: "))
promedio_parciales = (parcial1 + parcial2 + parcial3) / 3
examen_final = float(input("Introduce la nota del examen final: "))
trabajo_final = float(input("Introduce la nota del trabajo final: "))
calificacion_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)
print(f"La calificación final en la materia de Algoritmos es: {calificacion_final: }")
