import numpy as np

farenheits = np.array([32, 50, 68, 86, 104, 122, 140, 158, 176, 194, 212])
farenheits = np.random.randint(32, 213, size=20)

print(f'Farenheits: {farenheits} ºF')
#Vectorizada
celsius = (farenheits - 32) * 5/9

celsius_formateados = [f"{valor:.2f}" for valor in celsius]
print(f"Celsius: {celsius_formateados} ºC")

'''
Para vectorizar operaciones tamboen podemos usar la libreria Pandas y los Dataframes
'''
