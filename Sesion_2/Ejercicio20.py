print("=" * 12, "Proyección de edad futura", "=" * 11, "\n")
edad_actual = int(input("Ingrese su edad actual: "))

edad_en_5 = edad_actual + 5
edad_en_10 = edad_actual + 10
edad_en_20 = edad_actual + 20

print("=" * 19, "Resultados", "=" * 19, "\n")
print(f'{"Edad actual:":<36} {edad_actual:>13}')
print(f'{"Edad en 5 años:":<36} {edad_en_5:>13}')
print(f'{"Edad en 10 años:":<36} {edad_en_10:>13}')
print(f'{"Edad en 20 años:":<36} {edad_en_20:>13}')
print("=" * 50)