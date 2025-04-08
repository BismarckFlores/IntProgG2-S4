print("=" * 9, "Cálculo de precio con descuento", "=" * 8, "\n")
total_cuenta = float(input("Ingrese el total de la cuenta: $"))
propina = int(input("Ingrese el porcentaje de propina: "))

porcentaje_propina = propina / 100
monto_propina = porcentaje_propina * total_cuenta

print("=" * 19, "Resultados", "=" * 19, "\n")
print(f'{"Total de la cuenta:":<36} ${total_cuenta:>12,.2f}')
print(f'{"Porcentaje de propina:":<36} {propina:>12}%')
print(f'{"Monto de propina:":<36} ${monto_propina:>12,.2f}')
print("=" * 50)