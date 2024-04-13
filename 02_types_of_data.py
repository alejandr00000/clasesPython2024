#3. TIPOS DE DATOS. 

#A) String. Cadena de caracteres
lastname = 'Mejías'
print(lastname, type(lastname))

#B) Int (number). Números enteros
age = 40
print(age, type(age))

my_age = int(input('Ingrese su edad: '))
print(my_age, type(my_age))

#C) Boolean. Proposición lógica. True or false
is_monday = input('Ingrese el día de la semana: ').lower() == 'lunes'
print(is_monday, type(is_monday))

#D) Float. Números decimales
height = 1.78
print(height, type(height))

#E) List. Lista de objetos
vowels = ['a', 'e', 'i', 'o', 'u']
print(vowels, type(vowels))
print(vowels[0])

#Tuple. Lista de elementos.
my_tuple = ("a", "b", "c")
print(my_tuple, type(my_tuple))

#set. Lista de elementos.
my_set = {"a", "b", "c"}
print(my_set)
print(type(my_set))
