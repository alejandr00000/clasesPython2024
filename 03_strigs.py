'''
name = input('Ingrese su nombre: ').title()  #upper() lower()
print(name)
lastname = "Mejías Herrera"

#Tres formas de concatenar
answer01 = 'Hola, mi nombre es {} y mis apellidos son {}'.format(name,lastname)
print(answer01)

answer02 = 'Hola, mi nombre es ' + name + ' y mis apellidos son ' + lastname
print(answer02)

answer03 = f'Hola, mi nombre es {name} y mis apellidos son {lastname}'
print(answer03)

text = 'Volver al futuro es una gran película'
print(text)

#in text ve si el texto está en el string text.
print('futuro' in text) 

#Devuelve el número de caracteres que tiene.
size = len(text)
print(size)

#Transforma el texto a mayúsculas.
print(text.upper())

#Transforma el texto a minúsculas.
print(text.lower())

#Coloca la primera letra de cada palabra en mayúsculas.
print(text.title())

#Coloca la primera letra en mayúsculas.
print(text.capitalize())

#Cuenta cuántas veces está la letra 'a'
print(text.count('a'))

#Reemplaza un caarcter por otro
#print(text.replace('Volver al futuro', 'Inception'))
text = text.replace('Volver al futuro','Inception')
print(text)

#Extraer una parte de un string
string = "El hombre de negro huía a través del desierto,\ny el pistolero iba en pos de él"
print(string)

#Extraeremos los primeros dieciocho caracteres
extract01 = string[0:18] #No se incluye el 18
print(extract01)
#Extraeremos los últimmos 12 caracteres
extract02 = string[-12:]
print(extract02)
'''

#Rncontrar la primera o última posición de un caracter en un string
string ="Hola. Este es un mensaje de prueba"
first_position = string.find("e")
print(first_position)
last_position = string.rfind("e")
print(last_position)

