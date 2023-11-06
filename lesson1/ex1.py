# De 60 alumnos que rinden en 3 examenes (A,B y C)
# - 10 aprobarón solo A
# - 20 aprobarón A
# - 25 aprobarón B
# - 21 aprobarón C
# - 6 aprobarón B y C y no A
# - 7 aprobarón A y B
# - 3 aprobarón A, B y C
# ¿Cuantos desaprobarón los tres examenes?

#Numero total de alumnos
alumnos_totales= 60


aprobaron_solo_A = set(range(1, 11))  # Del 1 al 10
aprobaron_A = set(range(1, 21))  # Del 1 al 20
aprobaron_B = set(range(1, 26))  # Del 1 al 25
aprobaron_C = set(range(1, 22))  # Del 1 al 21
aprobaron_solo_B_C = set(range(1, 7))  # Del 1 al 6
aprobaron_A_B = set(range(1, 8))  # Del 1 al 7
aprobaron_A_B_C = set(range(1, 4))  # Del 1 al 3

# Solución
aprobaron_solo_A_B = len(aprobaron_A_B) - len(aprobaron_A_B_C)
aprobaron_solo_B = len(aprobaron_B) - aprobaron_solo_A_B - len(aprobaron_A_B_C) - len(aprobaron_solo_B_C)
aprobaron_solo_A_C = len(aprobaron_A) - len(aprobaron_A_B_C) - aprobaron_solo_A_B - len(aprobaron_solo_A)
aprobaron_solo_C = len(aprobaron_C) - len(aprobaron_A_B_C) - aprobaron_solo_A_C - len(aprobaron_solo_B_C)

print("Número de estudiantes que aprobaron SOLO A y B:", aprobaron_solo_A_B)
print("Número de estudiantes que aprobaron SOLO B:", aprobaron_solo_B)
print("Número de estudiantes que aprobaron SOLO A y C:", aprobaron_solo_A_C)
print("Número de estudiantes que aprobaron SOLO C:", aprobaron_solo_C)

