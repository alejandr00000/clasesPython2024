import math
import random

#Devuelve el número pi
pi = math.pi
print(pi)

#Devuelve un float aleatorio entre 0 y 1
number01 = random.random()
print(number01)

#Devuelve un float en el intervalo
number02 = random.uniform(1, 7)
print(number02)

#Devuelve un int en el intervalo
number03 = random.randint(1, 7)
print(number03)

#Devuelve un objeto aleatorio de una lista
people = ['Alan', 'Brenda', 'Catalina', 'Dante']
person = random.choice(people)
print(person)