'''
Crea una función que reciba una lista y la modifique eliminando el primer y último elementos. 
Esta función debe devolver None.  

Crea otra función que devuelva una nueva lista con todos los elementos excepto el primero y el último, 
sin modificar la lista original.
'''
import numpy as np
import pandas as pd

def modificar_lista(lista):
    lista.pop(0)  # Elimina el primer elemento
    lista.pop(-1)  # Elimina el último elemento
    return None

def nueva_lista_modificada(lista):
    return lista[1:-1]  # Devuelve una nueva lista sin el primer y último elemento

'''
numeros = [10, 20, 30, 40, 50]
Otros ejemplos
print(numeros[1:4]) #[20, 30, 40]
print(numeros[:3]) #[10,20,30]
print(numeros[2:]) #[30,40,50]
print(numeros[::2]) #[10,30,50]
'''


numeros = [1, 2, 3, 4, 5, 6]
print("Lista original:", numeros)

'''
modificar_lista(numeros)
print("Lista modificada:", numeros)
'''

nueva_lista = nueva_lista_modificada(numeros)
print("Nueva lista sin modificar la original:", nueva_lista)

#El mismo metodo funciona para numpy
data = np.array([1, 2, 3, 4, 5, 6])
print(nueva_lista_modificada(data))


#Pero que pasa con pandas? Funcion iloc
df  = pd.DataFrame({
    'valor': [1, 2, 3, 4, 5],
})

print(df)
df_modificado = df.iloc[1:-1]  # Selecciona todas las filas excepto la primera y la última
print("DataFrame modificado:")
print(df_modificado)
