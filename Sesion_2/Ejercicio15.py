print("=" * 9, "Cálculo de precio con descuento", "=" * 8, "\n")
nombre_producto = input("Ingrese el nombre del producto: ")
precio_producto = float(input("Digite el precio del producto: "))
descuento = int(input("Digite el descuento a aplicar: "))

descuento /= 100
descuento_aplicado = precio_producto * descuento
precio_final = precio_producto - descuento_aplicado

print("=" * 19, "Resultados", "=" * 19, "\n")
print(f'{"Producto:":<32} {nombre_producto:<16}')
print(f'{"Precio original:":<32} ${precio_producto:>16,.2f}')
print(f'{"Descuento aplicado:":<32} ${descuento_aplicado:>16,.2f}')
print(f'{"Precio final con descuento:":<32} ${precio_final:>16,.2f}')
print("=" * 50)