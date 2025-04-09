print("=" * 10, "Cálculo de salario del trabajador", "=" * 10, "\n")
nombre_trabajador = input("Ingrese el nombre del trabajador: ")
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
pago_por_hora = float(input("Ingrese el pago por hora: $"))

sueldo_bruto = horas_trabajadas * pago_por_hora
descuento_renta = sueldo_bruto * 0.05
salario_neto = sueldo_bruto - descuento_renta

print("=" * 15, "Resultados", "=" * 15, "\n")
print(f'{"Nombre del trabajador:":<36} {nombre_trabajador:>12}')
print(f'{"Sueldo bruto:":<36} ${sueldo_bruto:>12,.2f}')
print(f'{"Descuento renta (5%):":<36} ${descuento_renta:>12,.2f}')
print(f'{"Salario neto a pagar:":<36} ${salario_neto:>12,.2f}')
print("=" * 50)