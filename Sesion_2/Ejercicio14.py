print("=" * 12, "Cálculo de nuevo salario", "=" * 12, "\n")
salario_actual = float(input("Ingrese su salario actual: "))

incremento = salario_actual * 0.08
salario_incrementado = salario_actual + incremento
descuento_servicios = salario_incrementado * 0.025
nuevo_salario = salario_incrementado - descuento_servicios

print("\n")
print("=" * 19, "Resultados", "=" * 19)
print(f'{"Salario actual:":<36} ${salario_actual:>12,.2f}')
print(f'{"Incremento (8%):":<36} ${incremento:>12,.2f}')
print(f'{"Descuento por servicios (2.5%):":<36} ${descuento_servicios:>12,.2f}')
print(f'{"Nuevo salario:":<36} ${nuevo_salario:>12,.2f}')
print("="*50)