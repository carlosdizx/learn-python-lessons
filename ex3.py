# Conjunto de personas registradas para el taller de Python
taller_python = {"Alice", "Bob", "Charlie", "David", "Eva"}
# Conjunto de personas registradas para el taller de Data Science
taller_data_science = {"Bob", "Eva", "Frank", "Grace", "Helen"}
# Conjunto de personas registradas para la conferencia principal
conferencia_principal = {"Charlie", "David", "Grace", "Helen", "Isabel"}
# Conjunto de personas que se han registrado para al menos uno de los eventos
todos_registrados = taller_python.union(taller_data_science, conferencia_principal)

print("Todos los participantes", todos_registrados, "\n")

# Ahora, puedes realizar las siguientes operaciones:
# 1. Encuentra las personas que se han registrado tanto para el taller de Python como para el taller de Data Science.
# 2. Encuentra las personas que se han registrado para el taller de Python pero no para la conferencia principal.
# 3. Encuentra las personas que se han registrado para la conferencia principal pero no para el taller de Python ni el taller de Data Science.
# 4. Encuentra las personas que se han registrado solo para uno de los talleres (Python o Data Science) pero no para ambos.

# Solución
# 1.
python_and_data_science = taller_python.intersection(taller_data_science)
print("taller de Python y el taller de Data Science", python_and_data_science)

python_or_data_science = taller_python.difference(conferencia_principal)
print("Taller de python y no a la conferencia principal", python_or_data_science)

# 3.
only_conferencia_principal = conferencia_principal.difference(taller_python, taller_data_science)
print("Personas registradas solo en la conferencia principal:", only_conferencia_principal)

# 4.
registered_in_only_one_workshop = taller_python.symmetric_difference(taller_data_science)
print("Registrados en Python o en Data Science pero no en ambos:", registered_in_only_one_workshop)
