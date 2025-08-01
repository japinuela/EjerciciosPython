import pandas as pd

excel_file_path = './data/country_population.xlsx'
df_population = pd.read_excel(excel_file_path)


countries = df_population.values.tolist()

regions = {}
for country in countries:
    region = country[2]
    population = country[3]

    # if (pd.isna(region)):
    #   continue

    # if pd.isna(population):
    #     population = 0
    # else:
    #     try:
    #         population = int(population)
    #     except ValueError:
    #         population = 0

    regions[region] = regions.get(region, 0) + population



# Convertir el diccionario en DataFrame
df_regions = pd.DataFrame(list(regions.items()), columns=['region', 'population'])

# Guardar en CSV
output_path = './data/regions_population_collab.csv'
df_regions.to_csv(output_path, index=False)

print(f"Archivo guardado en: {output_path}")