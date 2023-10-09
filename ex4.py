# Conjunto de socios que juegan al fútbol
futbolistas = {"Alice", "Bob", "Charlie", "David", "Eva"}

# Conjunto de socios que juegan al baloncesto
baloncestistas = {"Bob", "Eva", "Frank", "Grace", "Helen"}

# Conjunto de socios que juegan al tenis
tenistas = {"Charlie", "David", "Grace", "Helen", "Isabel"}

futbol_y_baloncesto = futbolistas.intersection(baloncestistas)
futbol_o_baloncesto = futbolistas.difference(tenistas)
almenos_un_deporte = futbolistas.union(baloncestistas, tenistas)
exactamente_un_deporte = futbolistas.symmetric_difference(baloncestistas).symmetric_difference(tenistas)
exactamente_dos_deportes = futbol_y_baloncesto.union(futbolistas.intersection(tenistas)).union(
    tenistas.intersection(baloncestistas))

print("Juegan futbol y baloncesto:", futbol_y_baloncesto)
print("Juegan futbol o baloncesto:", futbol_o_baloncesto)
print("Juegan al menos 1 deporte:", almenos_un_deporte)
print("Juegan exactamente un deporte:", exactamente_un_deporte)
print("Juegan exactamente dos deportes:", exactamente_dos_deportes, len(exactamente_dos_deportes))