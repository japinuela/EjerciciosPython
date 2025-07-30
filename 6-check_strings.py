import pandas as pd
'''
6.	Crea una función que comprueba si una variable es un string y no está vacío:
print(check_valid_string(6)) # False
print(check_valid_string('Alvaro')) # true
'''

#Funcion 
def check_valid_string(value):
    return isinstance(value, str) and value.strip() != ''
    

print(check_valid_string(6))
print(check_valid_string('Alvaro'))
#¿Queremos que esto sea valido o que no lo sea? En ML y DS esto no es valido. Queremos que nos diga que esta mal.
print(check_valid_string('  '))

#2 validar strings con lambda
df = pd.DataFrame({'valor': ['Ana','','Luis', None, 123, 'Maria']})
df['es_valido'] = df['valor'].apply(lambda x: isinstance(x, str) and x.strip() != '')
print(df)