numeros_pares = {2, 4, 6, 8, 10}  # Conjunto de números pares del 1 al 10
numeros_impares = {1, 3, 5, 7, 9}  # Conjunto de números impares del 1 al 10
divisibles_por_3 = {3, 6, 9}  # Conjunto de números divisibles por 3 del 1 al 10
mayores_que_5 = {6, 7, 8, 9, 10}  # Conjunto de números mayores que 5 del 1 al 10

# Encuentra la unión de los conjuntos de números pares e impares.
# Encuentra la intersección entre los conjuntos de números pares y divisibles por 3.
# Encuentra la diferencia entre los conjuntos de números mayores que 5 y divisibles por 3.

# Solución
# 1.
numeros = numeros_pares.union(numeros_impares)
print("números pares o impares", numeros)

# 2.
divisibles_por_3_e_impares = numeros_impares.intersection(divisibles_por_3)
print("Divisibles por 3 e impares", divisibles_por_3_e_impares)

dif_mayores_que_5_y_divisibles_por_3 = mayores_que_5.difference(divisibles_por_3)
print("Diferentes mayores que 5 y no divisibles por 3", dif_mayores_que_5_y_divisibles_por_3)
