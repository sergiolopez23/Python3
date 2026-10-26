sueldo_base = float(input("Introduce el sueldo base: "))
venta1 = float(input("Venta 1: "))
venta2 = float(input("Venta 2: "))
venta3 = float(input("Venta 3: "))

total_ventas = venta1 + venta2 + venta3
comision = total_ventas * 0.10
total_mes = sueldo_base + comision
print(f"Dinero por comisiones: {comision}")
print(f"Total a recibir en el mes: {total_mes}")
