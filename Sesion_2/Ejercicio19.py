print("=" * 15, "Generador de correo", "=" * 14, "\n")
nombre = input("Ingrese su nombre: ").strip().lower()
apellido = input("Ingrese su apellido: ").strip().lower()

correo = f"{nombre}.{apellido}@miuniversidad.edu.ni"

print("=" * 19, "Resultado", "=" * 19, "\n")
print(f'{"Correo generado:"} {correo}')
print("=" * 50)