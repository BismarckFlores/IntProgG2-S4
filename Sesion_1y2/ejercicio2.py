#Tipos de datos numericos

cantidad = 10
precio = 130
total = cantidad * precio

def ftexto(texto):
    return f"{texto:<10}"

print(f'{"Cantidad:":<10} {cantidad:>6}')
print(f'{ftexto("Precio:")} {precio:>6}')
print(f'{ftexto("Total:")} {total:>6}')