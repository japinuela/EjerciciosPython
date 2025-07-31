'''
10.	Crea una función que, partiendo del texto de un paciente, 
genere un diccionario con información sobre el nombre, apellidos, edad, peso, altura y dolencia. 
El texto siempre tiene la misma estructura:
text = 'Juan Antonio Piñuela, 51 años, 1.70 de altura y 75 kilos; Resfriado en verano.'
'''

#Vamos a probar con expresiones regulares y clases
import re
from dataclasses import dataclass

@dataclass
class Paciente:
    nombre: str
    apellidos: str
    edad: int
    altura: float
    peso: float
    dolencia: str

def parsear_texto(texto: str) -> Paciente:
    # Extraer nombre y apellidos
    try:
        nombre_apellidos = re.search(r'^([A-Za-zÁÉÍÓÚáéíóúñÑ]+) ([A-Za-zÁÉÍÓÚáéíóúñÑ ]+),', texto)
        nombre = nombre_apellidos.group(1)
        apellidos = nombre_apellidos.group(2).strip()
    
        # Edad
        edad = int(re.search(r'(\d+) años', texto).group(1))
    
        # Altura
        altura = float(re.search(r'(\d+\.\d+) de altura', texto).group(1))
    
        # Peso
        peso = float(re.search(r'(\d+\.\d+) kilos', texto).group(1))

        # Dolencia
        dolencia = re.search(r'; (.+)\.', texto).group(1)
    except AttributeError as e:
        print("El formato del texto no es válido")
        return None
 
    return Paciente(nombre, apellidos, edad, altura, peso, dolencia)
 
# Ejemplo de uso
text = 'Juan Antonio Piñuela, 51 años, 1.70 de altura y 75.5 kilos; Resfriado en verano.'
paciente = parsear_texto(text)
if (paciente):
    print(paciente)