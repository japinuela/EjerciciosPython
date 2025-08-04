import re
from unidecode import unidecode
from collections import Counter

'''
Primera vez
import nltk
nltk.download('stopwords')
quit()
'''

from nltk.corpus import stopwords

def normalize(texto):
    '''
    - Convertir a minusculas
    - Eliminar acentos y caracteres especiales con unidecode
    - Expresiones regualress para puntuacin llevarlo a espacios y eliminar dobles especios
    '''
    texto = texto.lower()
    texto = unidecode(texto)
    texto = re.sub(r'[^\w\s]', ' ', texto)
    texto = re.sub(r'\s+', ' ', texto)
    '''
    Versión primera
    texto = re.sub(r"[.,;:¿?¡!\"'()\-\n]", " ", texto)  # reemplaza puntuación por espacios
    texto = re.sub(r"\s+", " ", texto)  # elimina dobles espacios
    '''

    return texto.strip()

def tokenize(text):
    return text.split()

def get_vocabulary(tokens):
    return set(tokens)

def count_words(tokens):
    return Counter(tokens)

#Falta cargar el fichero quijote.txt
# Cargar un fichero codificado en ANSI
with open('data/quijote.txt', encoding='latin1') as archivo:
    quijote = archivo.read()

# print(quijote[:500])
# quit()

texto_limpio = normalize(quijote)
palabras = tokenize(texto_limpio)

stop_words = set(stopwords.words('spanish'))
extra_stopwords = {"de", "y", "mas", "asi", "tan", "si", "habia", "tenia"}
stop_words.update(extra_stopwords)
palabras_filtradas = [palabra for palabra in palabras if palabra not in stop_words]

conteo = count_words(palabras_filtradas)
for palabra, frecuencia in conteo.most_common(100):
    print(f"{palabra}: {frecuencia}")