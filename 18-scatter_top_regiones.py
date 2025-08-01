import pandas as pd
import matplotlib.pyplot as plt
import math

# === 1️⃣ Leer datos ===
df = pd.read_excel('data/country_population.xlsx', usecols=['Country Name', 'Region', 'Population'])

# === 2️⃣ Crear ranking de población dentro de cada región ===
df['Rank'] = df.groupby('Region')['Population'].rank(method='first', ascending=False)

# === 3️⃣ Lista de regiones ===
regiones = df['Region'].unique()

# === 4️⃣ Configurar rejilla de subplots (4 columnas) ===
ncols = 4
nrows = math.ceil(len(regiones) / ncols)

fig, axes = plt.subplots(nrows, ncols, figsize=(ncols*5, nrows*4))
axes = axes.flatten()

colors = plt.cm.tab10.colors  # paleta automática

# === 5️⃣ Dibujar scatter por región y etiquetar top 3 ===
for idx, (ax, region) in enumerate(zip(axes, regiones)):
    datos_region = df[df['Region'] == region].sort_values('Population', ascending=False)
    
    # Scatter de todos los países de la región
    ax.scatter(datos_region['Rank'], datos_region['Population'], 
               color=colors[idx % len(colors)], alpha=0.7, edgecolor='k')
    
    # Poner etiquetas solo a los top 3
    top3 = datos_region.head(3)
    for _, fila in top3.iterrows():
        ax.text(fila['Rank'] + 0.1,      # desplazamiento a la derecha
                fila['Population'], 
                fila['Country Name'],
                fontsize=8,
                color='black')
    
    ax.set_title(region, fontsize=10)
    ax.set_xlabel("Ranking en la región")
    ax.set_ylabel("Población")
    ax.set_yscale('log')  # opcional para mejorar legibilidad
    ax.tick_params(axis='x', labelsize=8)
    ax.tick_params(axis='y', labelsize=8)

# === 6️⃣ Apagar los subplots vacíos ===
for i in range(len(regiones), len(axes)):
    axes[i].axis('off')

plt.tight_layout()
plt.show()
