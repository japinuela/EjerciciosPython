'''
9.	Escribe un programa que pregunte 5 números al usuario, los introduzca en una lista, 
e imprima la lista ordenada de menor a mayor y el valor medio y mediano
'''

import numpy as np

#Aprovechaos para controlar excepciones
while True:
    notas_input = input("Ingrese 5 números separados por comas: ")
    try:
        #List comprehension para convertir la entrada en una lista de números
        numeros = [float(n) for n in notas_input.split(",")]
        if len(numeros) != 5:
            print("Debes ingresar exactamente 5 números.")
            continue
        break
    except ValueError:
        print("Por favor, ingrese un número válido.")

arr = np.array(numeros)
# Calcular media y mediana
ordenado = np.sort(arr)
media = np.mean(arr)
mediana = np.median(arr)
minimo = np.min(arr)
maximo = np.max(arr)

#Desviacion estandar
desviacion = np.std(arr)
'''
Desviación estándar poblacional
\sigma = \sqrt{\frac{1}{N-1} \sum_{i=1}^{N} (x_i - \bar{x})^2}
SI lo llamo con ddof = 1- Cambia el divisor a N-1 >> Desviación estándar muestral (corrección)
'''
error_estandar = np.std(arr) / np.sqrt(len(arr))
cuartiles = np.quantile(arr, [0.25, 0.5, 0.75])

print("Lista ordenada:", ordenado)
print("Valor medio:", media)
print("Valor mediano:", mediana)
print("Cuartiles", cuartiles)


