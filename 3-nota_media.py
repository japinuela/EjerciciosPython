'''
3.	Escribe un programa para introducir las notas de una asignatura separadas por comas 
y obtener la calificación media siempre que todas ellas sean superiores a un valor mínimo 
que podemos establecer en 4.5 puntos. En caso de que no se alcance ese valor en una calificación 
la nota media será igual a ese valor inferior a 4.5
'''

NOTA_MIN = 4.5
notas = input("Introduce las notas separadas por comas: ")

#Quiero efectivamente que utiliceis list comprehensions
notas = [float(nota) for nota in notas.split(",")]

print(notas)
media = sum(notas) / len(notas)
if media < NOTA_MIN:
    media = 4.5

#FORMA 1. Bucle FOR nota in notas:
#FORMA 2. Lambda directo o con una función
#3,5,7 > La nota final es 3
#5,7,9 > La nota final es 7
print(f"La nota final es: {media}")
