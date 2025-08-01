import pandas as pd
import matplotlib.pyplot as plt

# 1️⃣ Leer el CSV con las regiones y la población total
df = pd.read_csv('data/region_population.csv')

# 2️⃣ Crear el gráfico de pastel
plt.figure(figsize=(8,8))
plt.pie(
    df['Population'], 
    labels=df['Region'], 
    autopct='%1.1f%%',        # formato del porcentaje
    startangle=140,           # ángulo inicial para que se vea mejor
    colors=plt.cm.Set3.colors # paleta de colores agradable
)

plt.title("Distribución de la Población Mundial por Región")
plt.axis('equal')  # 🔹 asegura que el pastel sea redondo

plt.show()
