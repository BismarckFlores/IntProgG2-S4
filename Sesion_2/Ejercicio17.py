print("=" * 12, "Cálculo de total con IVA", "=" * 12, "\n")
precio_producto_1 = float(input("Ingrese el precio del primer producto: $"))
precio_producto_2 = float(input("Ingrese el precio del segundo producto: $"))
precio_producto_3 = float(input("Ingrese el precio del tercer producto: $"))

subtotal = precio_producto_1 + precio_producto_2 + precio_producto_3
iva = subtotal * 0.15
total_a_pagar = subtotal + iva

print("=" * 19, "Resultados", "=" * 19, "\n")
print(f'{"Subtotal:":<36} ${subtotal:>12,.2f}')
print(f'{"IVA (15%):":<36} ${iva:>12,.2f}')
print(f'{"Total a pagar:":<36} ${total_a_pagar:>12,.2f}')
print("="*50)