import math

#Ingresar el radio de un círculo
r = float(input('Ingrese el radio de un círculo: '))

if r >= 0:
    #Preguntar si se quiere calcualar el área o el perímetro
    element = int(input('Ingrese 1 si desea calcular el área o 2 si quiere calcular el perímetro: '))

    if element == 1:
        result = math.pi*r**2
        print(result)
    elif element == 2:
        result = 2*math.pi*r
        print(result)
    else: 
        print('Error al ingresar datos')
else:
    print('El radio debe ser un número no negativo')