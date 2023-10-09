from matplotlib_venn import venn3
import matplotlib.pyplot as plt

# Tus conjuntos de datos
# Datos de ventas en la caja registradora 1
caja1_ventas = {"Producto A", "Producto B", "Producto C", "Producto D", "Producto E", "Producto F", "Producto G",
                "Producto H", "Producto I", "Producto J", "Producto K", "Producto L"}
# Datos de ventas en la caja registradora 2
caja2_ventas = {"Producto B", "Producto C", "Producto D", "Producto E", "Producto M", "Producto N", "Producto O",
                "Producto P", "Producto Q", "Producto R", "Producto S", "Producto T"}
# Datos de ventas en la caja registradora 3
caja3_ventas = {"Producto C", "Producto D", "Producto E", "Producto U", "Producto V", "Producto W", "Producto X",
                "Producto Y", "Producto Z"}

# Crea el primer diagrama de Venn para A, B y C
venn3([caja1_ventas, caja2_ventas, caja3_ventas], set_labels=('Caja 1', 'Caja 2', 'Caja 3'))
plt.title("Ventas en caja 1, 2 y 3")
plt.show()

productos_vendidos_en_todas_las_cajas = caja1_ventas.intersection(caja2_ventas, caja3_ventas)
almenos_una_venta = caja1_ventas.union(caja2_ventas, caja3_ventas)
solamente_en_caja_1 = caja1_ventas.difference(caja2_ventas).difference(caja3_ventas)
exactamente_dos_veces = caja1_ventas.intersection(caja2_ventas).union(caja1_ventas.intersection(caja3_ventas)).union(
    caja2_ventas.intersection(caja3_ventas)).difference(productos_vendidos_en_todas_las_cajas)

print("Vendidos en todas las cajas", productos_vendidos_en_todas_las_cajas, len(productos_vendidos_en_todas_las_cajas))
print("Vendidos almenos un vez", almenos_una_venta, len(almenos_una_venta))
print("Vendidos solamente en la caja 1", solamente_en_caja_1, len(solamente_en_caja_1))
print("Vendidos exactamente 2 veces", exactamente_dos_veces, len(exactamente_dos_veces))
