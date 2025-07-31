'''
13.	Dado el fichero country_population.xlsx utilice la librería Pandas para recorrer cada país y 
obtener el acumulado de población por región. Guarda los resultados en un archivo CSV 
llamado region_population.csv, con dos columnas: region y population. 
Resuelva el ejercicio de dos maneras:
a.	Con un diccionario que acumule en region[nombre] la población total.
b.	Con Pandas utilizando el método groupBy y sum
Resuelva el ejercicio en GoogleCollab para gestionar ficheros externos tanto de entrada como de salida.
'''

import pandas as pd

# Cargar el archivo Excel
df = pd.read_excel('./data/country_population.xlsx', usecols=['Country Name', 'Region', 'Population'])
print(df.head())

#agg_df = df.groupby('Region')['Population'].sum().reset_index()

agg_df = df.groupby('Region', as_index=False)['Population'].sum()
agg_df.to_csv('./data/region_population.csv', index=False)
