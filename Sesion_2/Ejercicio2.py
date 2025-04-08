a = 4
b = 6
c = 3

print("\nValores iniciales:")
print("a =", a)
print("b =", b)
print("c =", c)

print("\nPaso 1: Sumar a + b que están en el paréntesis")
suma = a + b
print(f"{a} + {b} = {suma}")

print("\nPaso 2: Multiplicar el resultado de la suma por c")
multiplicacion = suma * c
print(f"{suma} * {c} = {multiplicacion}")

print("\nPaso 3: Dividir el resultado entre 2")
resultado = multiplicacion / 2
print(f"{multiplicacion} / 2 = {resultado}")

print("\nResultado final de la expresión (a + b) * c / 2 =", resultado)