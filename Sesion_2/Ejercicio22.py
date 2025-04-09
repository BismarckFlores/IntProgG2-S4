print("=" * 13, "Cálculo de pulsaciones", "=" * 13, "\n")
edad = int(input("Ingrese su edad: "))

num_pulsaciones = (220 - edad) / 10

print("=" * 19, "Resultados", "=" * 19, "\n")
print(f'{"Pulsaciones cada 10 seg:":<37} {num_pulsaciones:>12,.2f}')
print("=" * 50)