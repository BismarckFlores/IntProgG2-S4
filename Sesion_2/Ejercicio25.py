print("=" * 5, "Distribución del presupuesto", "=" * 5, "\n")
presupuesto_total = float(input("Ingrese el presupuesto anual: $"))

urgencias = presupuesto_total * 0.37
pediatria = presupuesto_total * 0.42
traumatologia = presupuesto_total * 0.21

print("=" * 19, "Resultados", "=" * 19, "\n")
print(f'{"Urgencias (37%):":<36} ${urgencias:>12,.2f}')
print(f'{"Pediatría (42%):":<36} ${pediatria:>12,.2f}')
print(f'{"Traumatología (21%):":<36} ${traumatologia:>12,.2f}')
print("=" * 50)