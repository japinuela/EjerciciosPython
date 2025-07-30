'''
1.	Escribe un programa que use input para preguntarle al usuario su nombre y 
le dé la bienvenida con “Hola, Juan” usando print.
'''
print("#"*100)
nombre = input("¿Cuál es tu nombre? ")
print("Hola, " , nombre)

'''
F-strings
'''
print("-"*100)
print(f'Hola, {nombre.upper()}!')


print("-"*100)

precio = 45.6787787
print(f'El precio es {precio:.2f} €')
print(f'El precio es {precio:10.2f} €')  # 10 espacios, 2 decimales


print("-"*100)

persona = {"nombre": "Juan Antonio", "edad": 30}
print(f'Hola, {persona["nombre"]} tienes {persona["edad"]} años')
