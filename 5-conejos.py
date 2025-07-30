'''
5.	Un granjero tiene una pareja de conejos que cada 3 meses cría a otra pareja de conejos (que a su vez criará una pareja cada 3 meses de manera inmediata). 
Crea una función recursiva para calcular el número de conejos que tendrá el granjero después de 2 años (8 iteraciones)
Es decir, en el mes 0 (iteración 1) tiene 2 conejos, en el mes 3 (iteración 2), 4 conejos, en el mes 6 (iteración 3), 8 conejos…).
'''
#0 -> 1
#Mes 3, Trimestre 1 - 2 conejos
#Mes 6, Trimestre 2 - 4 conejos
#Mes 9, Trimestre 3 - 8 conejos
#Mes 12, Trimestre 4 - 16 conejos

def calculate_rabbits(trimestres):
    """Calcula el número de conejos después de un número de meses."""
    if trimestres <= 0:
        return 2  # En el mes 0, hay 2 conejos
    else:
        return calculate_rabbits(trimestres - 1) * 2
    
n = 0
while n < 8:
    print(f"Mes {n * 3}, Trimestre {n + 1} - {calculate_rabbits(n)} conejos")
    n += 1

#ME doy cuenta que el resultado es siempre 2^trimetre
calculate_rabbits_lambda = lambda t: 2 * (2 ** t)
n = 0
while n < 8:
    print(f"Mes {n * 3}, Trimestre {n + 1} - {calculate_rabbits_lambda(n)} conejos lambda")
    n += 1