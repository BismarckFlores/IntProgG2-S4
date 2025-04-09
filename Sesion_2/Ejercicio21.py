print("=" * 17, "Cálculo de masa", "=" * 16, "\n")
presion = float(input("Ingrese la presión: "))
volumen = float(input("Ingrese el volumen: "))
temperatura = float(input("Ingrese la temperatura: "))

masa = (presion * volumen) / (0.37 * (temperatura + 460))

print("=" * 19, "Resultados", "=" * 19, "\n")
print(f'{"Masa calculada:":<37} {masa:>12,.2f}')
print("=" * 50)