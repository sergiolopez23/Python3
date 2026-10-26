total_compra = float(input("Introduce el total de la compra: "))
descuento = total_compra * 0.15
total_pagar = total_compra - descuento
print(f"El descuento aplicado es de: {descuento: } €")
print(f"El total que deberá pagar finalmente es: {total_pagar: } €")
