# if (condition):
#     # Code to be executed if condition is True
# else:
#     # Code to be executed if condition is False

pet = input("¿cuál es tu mascota favorita? ")

if (pet =="perro"):
  print("Genial. Tienes buen gusto")
elif (pet == "gato"):
  print("espero que tengas suerte")
elif (pet == "hamster"):
  print("¿qué es esto?")
else:
  print("No tienes una mascota interesante")

stock = int(input("Digita tu stock"))

if(stock > 100 and stock < 200):
  print("El stock es correcto")
else:
  print("El stock es incorrecto")

num = int(input("Ingresa un número"))

if(num % 2 == 0):
  print("El número es par")
else:
  print("El número es impar")
  
