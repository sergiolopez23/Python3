precios = []
print("--- PRECIOS DE LOS ARTÍCULOS ---")
for i in range(5):
    precio = float(input(f"Introduce el precio del artículo {i + 1}: "))
    precios.append(precio)

cantidades = []
print("\n--- CANTIDADES VENDIDAS POR SUCURSAL ---")
for s in range(4):
    fila_sucursal = []
    print(f"Sucursal {s + 1}:")
    for a in range(5):
        cant = int(input(f"  Cantidad vendida del artículo {a + 1}: "))
        fila_sucursal.append(cant)
    cantidades.append(fila_sucursal)

print("\n================ INFORME DE VENTAS ================")

print("\n1. Cantidad total vendida de cada artículo:")
for a in range(5):
    total_articulo = sum(cantidades[s][a] for s in range(4))
    print(f"   - Artículo {a + 1}: {total_articulo} unidades")

total_sucursal_2 = sum(cantidades[1])
print(f"\n2. Cantidad total de artículos vendidos en la Sucursal 2: {total_sucursal_2}")

print(f"\n3. Cantidad del Artículo 3 en la Sucursal 1: {cantidades[0][2]}")

recaudaciones = []
print("\n4. Recaudación total por sucursal:")
for s in range(4):
    recaudacion_suc = sum(cantidades[s][a] * precios[a] for a in range(5))
    recaudaciones.append(recaudacion_suc)
    print(f"   - Sucursal {s + 1}: {recaudacion_suc:.2f} €")

recaudacion_empresa = sum(recaudaciones)
print(f"\n5. Recaudación total de la empresa: {recaudacion_empresa:.2f} €")

mayor_recaudacion = max(recaudaciones)
sucursal_ganadora = recaudaciones.index(mayor_recaudacion) + 1
print(f"\n6. La sucursal de mayor recaudación es la Sucursal {sucursal_ganadora} ({mayor_recaudacion:.2f} €).")
