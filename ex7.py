from matplotlib_venn import venn3
import matplotlib.pyplot as plt

electrica_estudiantes = {"Ana", "Luis", "María", "Elena", "Ricardo", "Sofía"}
matematicas_estudiantes = {"Carlos", "Elena", "Pedro", "Sofía", "Javier", "Ernesto"}
computacion_estudiantes = {"Juan", "María", "Carlos", "Ana", "Pedro", "Elena", "Luis", "Ernesto", "Bryan", "Edwin"}

conjunto_mas_grande = max(len(computacion_estudiantes), len(electrica_estudiantes), len(matematicas_estudiantes))
venn3([electrica_estudiantes, matematicas_estudiantes, computacion_estudiantes],
      set_labels=('Matematicas', 'Electrica', 'Computacion'), set_colors=('#0000FF', '#00FF00', '#FF0000'), alpha=0.7)
plt.title("Estudiantes por departamento")
plt.gcf().set_size_inches(10, 10)
plt.show()

# Solución
# 1

estudiantes_en_dos_departamentos = computacion_estudiantes.intersection(matematicas_estudiantes).union(
    computacion_estudiantes.intersection(electrica_estudiantes)).union(
    matematicas_estudiantes.intersection(electrica_estudiantes)).difference(
    matematicas_estudiantes.intersection(computacion_estudiantes,
                                         electrica_estudiantes))

estudiantes_en_un_departamento = computacion_estudiantes.symmetric_difference(
    matematicas_estudiantes).symmetric_difference(electrica_estudiantes).difference(
    computacion_estudiantes.intersection(matematicas_estudiantes, electrica_estudiantes))

estudiantes_en_comoputacion_matematicas_electrica = computacion_estudiantes.intersection(matematicas_estudiantes,
                                                                                         electrica_estudiantes)

estudiantes_solo_computacion = computacion_estudiantes.difference(matematicas_estudiantes).difference(
    electrica_estudiantes)

estudiantes_solo_matematicas = matematicas_estudiantes.difference(computacion_estudiantes).difference(
    electrica_estudiantes)

estudiantes_solo_electrica = electrica_estudiantes.difference(computacion_estudiantes).difference(
    matematicas_estudiantes)

estudiantes_computacion_y_electrica = computacion_estudiantes.intersection(electrica_estudiantes).difference(
    estudiantes_en_comoputacion_matematicas_electrica)

estudiantes_matematicas_en_otros_departamentos = matematicas_estudiantes.intersection(computacion_estudiantes,
                                                                                      electrica_estudiantes)

total_estudiantes_con_un_solo_programa = len(estudiantes_solo_matematicas.union(estudiantes_solo_electrica).union(
    estudiantes_solo_computacion))

print("Estudiantes en dos departamentos académicos", estudiantes_en_dos_departamentos)
print("Estudiantes en un solo departamento académico", estudiantes_en_un_departamento)
print("Estudiantes en los tres departamentos", estudiantes_en_comoputacion_matematicas_electrica)
print("Estudiantes solo de computacion: ", len(estudiantes_solo_computacion), "|", "matematicas:",
      len(estudiantes_solo_matematicas), "|", "electrica:", len(estudiantes_solo_electrica))
print("Estudiantes de solo computacion e ingenieria electrica:", estudiantes_computacion_y_electrica)
print("Estudiantes de matematicas en otros programas academicos:", estudiantes_matematicas_en_otros_departamentos)
print("Total de estudiantes unicos por departamento", total_estudiantes_con_un_solo_programa)
