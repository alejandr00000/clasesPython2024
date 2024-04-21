#En este archivo se mostrarán algunas funciones especiales que pueden ser utilizadas en una sola línea

#Función lambda
#Sintaxis
#nombreFuncion = lambda parámetro : return
#Por ejemplo, realizaremos una función lambda que reciba un número y retorne su cuadrado perfecto.
cuadrado = lambda x : x**2

numero01 = cuadrado(8)
print(numero01)

#Otro ejemplo, donde recibe dos números y retorma su producto
multiplicacion = lambda x, y : x*y

numero02 = multiplicacion(5, 8)
print(numero02)


#Función map
#Sintaxis
#nombreFuncion = map(function, iterables)
#nombreFuncion = list(map(function, iterables)) si quiere que muestre una lista
#Por ejemplo, se utilizará para obtener los cuadrados perfectos de una lista de valores

lista01 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_cuadrados = list(map(lambda x : x**2, lista01))
print(lista_cuadrados)

#Se puede hacer utilizando la función lambda creada anteriormente, para no tener que escribirla dentro de map
lista_cuadrados02 = list(map(cuadrado, lista01))
print(lista_cuadrados02)


#Función filter
#Sintaxis
#nombreFuncion = filter(funcion, iterable)
#Filter selecciona a los elementos que cumplen una condición en específico
#Por ejemplo, se utilizará la función filter para seleccionar los números mayores o iguales a cuatro de una lista

lista02 = [4.5, 6.8, 3.8, 5.2, 2.9, 3.3, 6.1]
lista_aprobados = list(filter(lambda x : x >= 4, lista02))
print(lista_aprobados)




