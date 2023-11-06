from matplotlib_venn import venn3
import matplotlib.pyplot as plt

# Tus conjuntos de datos
equipo_proyecto_A = {"Juan", "María", "Carlos", "Ana", "Pedro"}
equipo_proyecto_B = {"Ana", "Luis", "María", "Elena", "Ricardo"}
equipo_proyecto_C = {"Carlos", "Elena", "Pedro", "Sofía", "Javier"}

# Crea el primer diagrama de Venn para A, B y C
venn3([equipo_proyecto_A, equipo_proyecto_B, equipo_proyecto_C], set_labels=('Proyecto A', 'Proyecto B', 'Proyecto C'))
plt.title("Diagrama de Venn para Proyectos A, B y C")
plt.show()
