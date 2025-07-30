'''
7.	Crea una función para normalizar strings (minúsculas, quitar las tildes de las vocales, eliminar puntos y comas…).
'''

import pandas as pd
from unidecode import unidecode
import re
 
def normalize(text):
    if not isinstance(text, str):
        return ""
    
    # Convertir a minúsculas
    text = text.lower()
    # Quitar tildes y caracteres especiales
    text = unidecode(text)
    # Eliminar puntos, comas, punto y coma y otros signos de puntuación
    text = re.sub(r'[.,;:!?]', '', text)
    text = text.replace("-", " ")
    # Eliminar espacios extra
    text = text.strip()
    return text
 
# Crear el DataFrame
df = pd.DataFrame({'nombre': ['Álvaro, Sánchez...', 'María-José', ' CRÈME brûlée', None, 'Niño; Pérez']})
 
# Aplicar la función de normalización
df['nombre_normalizado'] = df['nombre'].apply(normalize)
 
print(df)