'''
2.	Gestión de inventario de una tienda
•	Crea un diccionario con los productos de una tienda y sus precios (al menos 5 productos).
•	Aplica un descuento del 10% a todos los precios.
•	Convierte los datos a una tabla y añade una columna con el precio rebajado.
•	Filtra y muestra solo los productos cuyo precio rebajado sea mayor a 20.
'''
import pandas as pd

# 1) Crear un diccionario con productos y precios
productos = {
    'Manzanas': 30,
    'Peras': 25,
    'Plátanos': 15,
    'Naranjas': 22,
    'Uvas': 18
}

# 2) Aplicar un descuento del 10% a todos los precios
descuento = 0.10
productos_descuento = {producto: precio * (1 - descuento) for producto, precio in productos.items()}


#3) Convertir los datos a una tabla
#df_productos = pd.DataFrame(list(productos_descuento.items()), columns=['Producto', 'Precio Rebajado'])
# 4) Filtrar productos con precio rebajado mayor a 20


df_productos = pd.DataFrame({
    "Producto": list(productos.keys()),
    "Precio": list(productos.values()),
    "Precio Rebajado": list(productos_descuento.values())
})

#Filtro DE TODO LA VIDA
df_filtrado = df_productos[df_productos['Precio Rebajado'] > 20]
# Mostrar resultados
print(df_filtrado)

