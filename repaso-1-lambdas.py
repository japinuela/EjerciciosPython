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
temperaturas_celsius = np.random.randint(-6, 41, size=15)

#Aqui lo hacemos todo con DataFrames
df = pd.DataFrame({"Celsius": temperaturas_celsius})
#Con dataFrames puede vectorizar son mas
df["Fahrenheit"] = df["Celsius"] * 9/5 + 32

#CLASICO. Un apply con lambda para generar una columna
df["Etiqueta"] = df["Celsius"].apply(lambda x: "Frío" if x < 10 else "Agradable" if 10 <= x <= 25 else "Calor")

print(df)