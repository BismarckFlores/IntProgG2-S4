print("=" * 12, "Cálculo de total con IVA", "=" * 12, "\n")
precios_productos = []
for i in range (1, 4):
    precio = float(input(f"Ingrese el precio del producto {i}: $"))
    precios_productos.append(precio)

subtotal = sum(precios_productos)
iva = subtotal * 0.15
total_a_pagar = subtotal + iva

print("=" * 19, "Resultados", "=" * 19, "\n")
print(f'{"Subtotal:":<36} ${subtotal:>12,.2f}')
print(f'{"IVA (15%):":<36} ${iva:>12,.2f}')
print(f'{"Total a pagar:":<36} ${total_a_pagar:>12,.2f}')
print("="*50)