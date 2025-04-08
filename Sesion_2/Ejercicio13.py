print("=" * 50)
cantidad_mujeres = int(input("\nIngrese la cantidad de mujeres en el aula: "))
cantidad_hombres = int(input("\nIngrese la cantidad de hombres en el aula: "))

total_estudiantes = cantidad_hombres + cantidad_mujeres
porcentaje_mujeres = (cantidad_mujeres / total_estudiantes) * 100
porcentaje_hombres = (cantidad_hombres / total_estudiantes) * 100

print("\n")
print("=" * 20, "Resultados", "=" * 20)
print(f'\nAlumnos en el aula: {total_estudiantes} Alumnos')
print(f'\nPorcentaje de mujeres en el aula: {porcentaje_mujeres:.2f}%')
print(f'\nPorcentaje de hombres en el aula: {porcentaje_hombres:.2f}%\n')
print("=" * 50)