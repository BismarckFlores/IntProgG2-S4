print("=" * 11, "Cálculo de precio de venta", "=" * 11, "\n")
precio_compra = float(input("Ingrese el precio de compra: $"))

ganancia = precio_compra * 0.30
precio_venta = precio_compra + ganancia

print("=" * 19, "Resultados", "=" * 19, "\n")
print(f'{"Precio de compra:":<36} ${precio_compra:>12,.2f}')
print(f'{"Ganancia (30%):":<36} ${ganancia:>12,.2f}')
print(f'{"Precio de venta:":<36} ${precio_venta:>12,.2f}')
print("=" * 50)