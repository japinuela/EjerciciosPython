'''
1.	Análisis de temperaturas. 
•	Genera 15 temperaturas aleatorias en grados Celsius (entre -5 y 40).
•	Convierte esas temperaturas a grados Fahrenheit.
•	Crea una lista de etiquetas que indiquen:
o	“Frío” si la temperatura en °C es menor a 10
o	“Agradable” si está entre 10 y 25
o	“Calor” si es mayor a 25
'''

import numpy as np
import pandas as pd
 
# Generar 15 temperaturas aleatorias en grados Celsius entre -5 y 40
temperaturas_celsius = np.random.uniform(-5, 40, 15)
temperaturas_celsius = np.random.randint(-6, 41, size=15)

# Convertir a grados Fahrenheit --- Vectorizado al ser numpu
temperaturas_fahrenheit = temperaturas_celsius * 9/5 + 32
 
'''
Solucion Marco
# Crear etiquetas según el rango de temperatura en Celsius
etiquetas = pd.cut(
    temperaturas_celsius,
    bins=[-np.inf, 10, 25, np.inf],
    labels=["Frío", "Agradable", "Calor"]
)
'''
etiquetas =  ["Frío" if temp < 10 else "Agradable" if 10 <= temp <= 25 else "Calor" for temp in temperaturas_celsius]
 
# Crear un DataFrame con los resultados
df = pd.DataFrame({
    "Celsius": temperaturas_celsius,
    "Fahrenheit": temperaturas_fahrenheit,
    "Etiqueta": etiquetas
})
 
# Mostrar el DataFrame
print(df)