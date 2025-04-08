monto_prestamo = 10000
tasa_interes_anual = 27

interes = (tasa_interes_anual / 100) * monto_prestamo

print("=" * 50)
print(f'\n{"Monto del prestamo: ":<30} ${monto_prestamo:>8}')
print(f'\n{"Tasa de interés anual: ":<30} {tasa_interes_anual:>8}%')
print(f'\n{"Interés a pagar en un año: ":<30} ${interes:>8}\n')
print("=" * 50)