anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
anio_actual = int(input("Ingrese el año actual: "))

edad_actual = anio_actual - anio_nacimiento
edad_futuro = (anio_actual + 10) - anio_nacimiento

print(f'Tu edad es de {edad_actual} y dentro de 10 años tendras {edad_futuro}')