mi_set = {1, 2, 3, 4, 5}
print(mi_set)

otro_set = set([1, 2, 3, 4, 5])
print(otro_set)

mi_set = {1, 2, 3}

# Agregar un elemento
mi_set.add(4)
print(mi_set)  # Salida: {1, 2, 3, 4}

# Eliminar un elemento
mi_set.remove(2)
print(mi_set)  # Salida: {1, 3, 4}

# Usar discard (no generará error si el elemento no existe)
mi_set.discard(5)  # No hace nada porque 5 no está en el set
print(mi_set)  # Salida: {1, 3, 4}


set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Unión
union = set_a | set_b
print(union)  # Salida: {1, 2, 3, 4, 5}

# Intersección
interseccion = set_a & set_b
print(interseccion)  # Salida: {3}

# Diferencia
diferencia = set_a - set_b
print(diferencia)  # Salida: {1, 2}

# Diferencia simétrica
diferencia_simetrica = set_a ^ set_b
print(diferencia_simetrica)  # Salida: {1, 2, 4, 5}