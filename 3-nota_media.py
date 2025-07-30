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


#FORMA 1. Bucle FOR nota in notas:
#FORMA 2. Lambda directo o con una función
#3,5,7 > La nota final es 3
#5,7,9 > La nota final es 7

media = (lambda n: sum(n)/len(n) if all(x >= NOTA_MIN for x in n) else min(n))(notas)


#media = (lambda n: .... )(notas)
print(f"La nota final es: {media:.2f}")
