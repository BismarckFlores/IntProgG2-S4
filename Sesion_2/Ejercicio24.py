print("=" * 7, "Cálculo de tiempo promedio semanal", "=" * 7, "\n")
lunes = float(input("Ingrese el tiempo del lunes (min): "))
miercoles = float(input("Ingrese el tiempo del miércoles (min): "))
viernes = float(input("Ingrese el tiempo del viernes (min): "))

tiempo_promedio = (lunes + miercoles + viernes) / 3

print("=" * 19, "Resultados", "=" * 19, "\n")
print(f'{"Promedio semanal:":<33} {tiempo_promedio:>12,.2f} min')
print("=" * 50)