#listas sirven para almacenar datos de diversos tipos.
#las listas se crean con corchetes [ ]
numbers = [1, 2, 3, 4, 5]
print(numbers)
print(type(numbers))

books = ['La carretera', 'Drácula', 'Cien años de soledad']
print(books)
print(type(books))

types = [1, True, "hola"]
print(types)
print(type(types))

#Identificar el tamaño de una lista
print(len(numbers))

#Extraer un elemento de la lista
print(numbers[0])
print(books[1])
print(types[2])

#Las listas son mutables, es decir, se pueden modificar
books[0] = 'La guerra de los mundos'
print(books)

#Reemplazar el último valor
print(numbers)
numbers[-1] = 10
print(numbers)

#Agregar un valor al final
numbers.append(23)
print(numbers)

#Agrega un elemento en una posición específica
numbers.insert(3, 31)
print(numbers)

#fusiona listas
numbers_02 = [2, 3, 5, 7, 11]
new_numbers = numbers + numbers_02
print(new_numbers)

#buscar un elemento y cambiarlo (Sólo cambia la primera aparición del elemento)
index = new_numbers.index(2)
new_numbers[index] = 15
print(new_numbers)

#Quitar un elemento específico
new_numbers.remove(7)
print(new_numbers)

#Quitar el último elemento de la lista
new_numbers.pop()
print(new_numbers)

#Quitar un elemento de una posición específica
new_numbers.pop(0)
print(new_numbers)

#Invertir el orden de la lista
new_numbers.reverse()
print(new_numbers)

#Ordenar una lista de menor a mayor
numbers_squares = [0, 36, 4, 1, 49, 9, 81, 16, 100, 25]
numbers_squares.sort()
print(numbers_squares)

#Ordenar una lista de strings
strings = ["re", "ab", "ed"]
strings.sort()
print(strings)

#sort no funciona con listas que tengan tipos de datos mezclados

#Une una lista a otra
numbers_squares.extend(strings)
print(numbers_squares)

#Vaciar una lista
numbers_squares.clear()
print(numbers_squares)

#Reemplaza un caracter por un arreglo, separando por palabras
names = "María Javier Antonia Camila Pablo"
print(names.split())