numbers = (1, 2, 3, 4, 5)
strings = ('Marcela', 'Rodrigo', 'Sandra', 'Nicolás')
print(numbers)
print(type(numbers))
print(strings)
print(type(strings))


print("Primer elemento =>", numbers[0])
print("Último elemento =>", numbers[-1])

#se ouede buscar elementos, pero no moficarlos
#Buscar la posición
print(strings.index('Sandra'))
#Contar cuántas veces está
print(strings.count('Nicolás'))

#transformar a lista
my_list = list(strings)
print(my_list)