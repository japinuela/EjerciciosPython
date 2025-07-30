import pandas as pd
df = pd.DataFrame({'nombre': ['Ana','Luis','Maria'], 'edad':[23, 35, 29]})
print(df)

#Aplicar una transformación a una columna
df['grupo_edad'] = df['edad'].apply(lambda x: 'Joven' if x < 30 else 'Adulto')
print(df)

# Calcular la media de edad por grupo usando lambda
medias = df.groupby('grupo_edad')['edad'].apply(lambda x: x.mean())
print(medias)

'''
menores = list(filter(lambda x: x < 30, df['edad']))
print(menores)

menores = df[df['edad'] < 30]
print(menores)
'''
