'''
2.	Escribe un programa que pregunte por la temperatura en Fahrenheit, convierta la temperatura a grados Celsius y la imprima
# formula fahrenheit to celsius (xºF − 32) * 5/9 = yºC
'''
#Es mejor usar funciones para reutilizar el código
def fahrenheit_a_celsius(fahrenheit):
    """Convierte Fahrenheit a Celsius."""
    return (fahrenheit - 32) * 5/9

fahrenheit = input("Introduce la temperatura en Fahrenheit: ")
#Es vital usar el tipo de datos adecuado para realizar cálculos
fahrenheit = float(fahrenheit)
print(f'La temperatura en Celsius es: {fahrenheit_a_celsius(fahrenheit):.2f} °C')

