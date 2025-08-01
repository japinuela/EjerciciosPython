import pandas as pd
import matplotlib.pyplot as plt
import math

# === 1️⃣ Leer datos ===
df = pd.read_excel('./data/country_population.xlsx', usecols=['Country Name', 'Region', 'Population'])

# === 2️⃣ Ordenar y obtener los 3 países más poblados por región ===
top3 = (df.sort_values(['Region', 'Population'], ascending=[True, False])
          .groupby('Region')
          .head(3))

# === 3️⃣ Lista de regiones ===
regiones = top3['Region'].unique()

# === 4️⃣ Definir cuántas columnas queremos (ej. 6) ===
ncols = 4
nrows = math.ceil(len(regiones) / ncols)

# === 5️⃣ Crear la figura y los subplots ===
fig, axes = plt.subplots(nrows, ncols, figsize=(ncols*4, nrows*4))  # tamaño dinámico
axes = axes.flatten()  # para iterar fácilmente
colors = plt.cm.tab20.colors   # paleta con 20 colores distintos

# === 6️⃣ Graficar cada región en su subplot ===
for idx, (ax, region) in enumerate(zip(axes, regiones)):
    datos_region = top3[top3['Region'] == region]
    color = colors[idx % len(colors)]  # asigna color según índice
    ax.bar(datos_region['Country Name'], datos_region['Population'], color=color)
    ax.set_title(region, fontsize=10)
    ax.tick_params(axis='x', rotation=45, labelsize=8)
    ax.set_ylabel("Población")

# === 7️⃣ Si sobran subplots vacíos, los apagamos ===
for i in range(len(regiones), len(axes)):
    axes[i].axis('off')

plt.tight_layout()
plt.show()
