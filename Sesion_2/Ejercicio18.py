print("=" * 15, "Calificación final", "=" * 15, "\n")
tareas = float(input("Ingrese la nota de tareas: "))
examen_parcial = float(input("Ingrese la nota del parcial: "))
examen_final = float(input("Ingrese la nota del examen final: "))

calificacion_final = (tareas * 0.30) + (examen_parcial * 0.30) + (examen_final * 0.40)

print("=" * 19, "Resultados", "=" * 19, "\n")
print(f'{"Nota de tareas (30%):":<36} {tareas:>13,.2f}')
print(f'{"Examen parcial (30%):":<36} {examen_parcial:>13,.2f}')
print(f'{"Examen final   (40%):":<36} {examen_final:>13,.2f}')
print("-" * 50)
print(f'{"Calificación final:":<36} {calificacion_final:>13,.2f}')
print("=" * 50)