import json
import sys
import csv
import os
import requests

def get_data_from_api(date):
    print("#"*100)
    print(f" 1. Downloading from API")
    print("#"*100)

    cities = {
        "A Coruña" : (43.37012643, -8.39114853),
        "Albacete" : (38.99588053, -1.85574745),
        "Alicante / Alacant" : (38.34548705, -0.4831832),
        "Almería" : (36.83892362, -2.46413188),
        "Ávila" : (40.65586958, -4.69771277),
        "Badajoz" : (38.87874339, -6.97099704),
        "Barcelona" : (41.38424664, 2.17634927),
        "Bilbao" : (43.25721957, -2.92390606),
        "Burgos" : (42.34113004, -3.70419805),
        "Cáceres" : (39.47316762, -6.37121092),
        "Cádiz" : (36.52171152, -6.28414575),
        "Castellón de la Plana / Castelló de la Plana" : (39.98640809, -0.03688142),
        "Ceuta" : (35.88810209, -5.30675127),
        "Ciudad Real" : (38.98651781, -3.93131981),
        "Córdoba" : (37.87954225, -4.78032455),
        "Cuenca" : (40.07653762, -2.13152306),
        "Girona" : (41.98186075, 2.82411899),
        "Granada" : (37.17641932, -3.60001883),
        "Guadalajara" : (40.63435548, -3.16210273),
        "Huelva" : (37.26004113, -6.95040588),
        "Huesca" : (42.14062739, -0.40842276),
        "Jaén" : (37.7651913, -3.7903594),
        "Las Palmas de Gran Canaria" : (28.09937855, -15.41336841),
        "León" : (42.59912097, -5.56707631),
        "Lleida" : (41.61527355, 0.62061934),
        "Logroño" : (42.46644945, -2.44565538),
        "Lugo" : (43.0091282, -7.55817392),
        "Madrid" : (40.40841191, -3.68760088),
        "Málaga" : (36.72034267, -4.41997511),
        "Melilla" : (35.294731, -2.942281),
        "Murcia" : (37.98436361, -1.1285408),
        "Ourense" : (42.33654919, -7.86368375),
        "Oviedo" : (43.36232165, -5.84372206),
        "Palencia" : (42.0078373, -4.53460106),
        "Palma" : (39.57114699, 2.65181698),
        "Pamplona / Iruña" : (42.814102, -1.6451528),
        "Pontevedra" : (42.43381442, -8.64799018),
        "Salamanca" : (40.96736822, -5.66538084),
        "San Sebastián / Donostia" : (43.31717158, -1.98191785),
        "Santa Cruz de Tenerife" : (28.46285408, -16.24720629),
        "Santander" : (43.46297885, -3.80474784),
        "Segovia" : (40.9498703, -4.12524116),
        "Sevilla" : (37.38620512, -5.99251368),
        "Soria" : (41.76327912, -2.46624798),
        "Tarragona" : (41.11910287, 1.2584219),
        "Teruel" : (40.34412951, -1.10927177),
        "Toledo" : (39.85715187, -4.02431421),
        "Valencia" : (39.47534441, -0.37565717),
        "Valladolid" : (41.65232777, -4.72334924),
        "Vitoria-Gasteiz" : (42.85058789, -2.67275685),
        "Zamora" : (41.49913956, -5.75494831),
        "Zaragoza" : (41.65645655, -0.87928652)
    }



    #GET https://archive-api.open-meteo.com/v1/archive?latitude=40.4168&longitude=-3.7038&start_date=2023-07-01&end_date=2023-07-31&daily=temperature_2m_max,temperature_2m_min&timezone=Europe/Madrid

    '''
    lat = 40.4168
    lon = -3.7038
    theURL = f"https://archive-api.open-meteo.com/v1/era5?latitude={lat}&longitude={lon}&start_date={date}&end_date={date}&daily=temperature_2m_max,temperature_2m_min,rain_sum,snowfall_sum,windspeed_10m_max&hourly=temperature_2m&timezone=Europe/Madrid"
    print(theURL)
    '''
    
    #cities = dict(list(cities.items())[:3])

    # Lista para almacenar los resultados
    results = []

    # Iterar sobre cada ciudad
    for city, (lat, lon) in cities.items():
        # Construcción de la URL
        theURL = (
            f"https://archive-api.open-meteo.com/v1/era5?"
            f"latitude={lat}&longitude={lon}&start_date={date}&end_date={date}"
            f"&daily=temperature_2m_max,temperature_2m_min,rain_sum,snowfall_sum,windspeed_10m_max"
            f"&timezone=Europe/Madrid"
        )

        # Llamada a la API
        response = requests.get(theURL)

        if response.status_code == 200:
            data = response.json()

            # Obtener los valores diarios
            daily = data.get("daily", {})
            results.append({
                "Ciudad": city,
                "Fecha": date,
                "Temp Max (°C)": daily.get("temperature_2m_max", [""])[0],
                "Temp Min (°C)": daily.get("temperature_2m_min", [""])[0],
                "Precipitación (mm)": daily.get("rain_sum", [""])[0],
                "Nieve (mm)": daily.get("snowfall_sum", [""])[0],
                "Viento Máx (km/h)": daily.get("windspeed_10m_max", [""])[0]
            })
        else:
            print(f"Error al obtener datos para {city}: {response.status_code}")
        


    with open(f"daily_{date}.csv", mode="w", newline="", encoding="utf-8") as file:
        fieldnames = ["Ciudad", "Fecha", "Temp Max (°C)", "Temp Min (°C)", "Precipitación (mm)", "Nieve (mm)", "Viento Máx (km/h)"]
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter="|")
        writer.writeheader()
        writer.writerows(results)

    print("Archivo CSV generado correctamente.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        date = input("Introduzca la fecha (YYYY-MM-DD): ")
    else:
        date = sys.argv[1]  # yyyy-MM-dd

    get_data_from_api(date)
