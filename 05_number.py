#INTEGER

lives = 3
print(lives,type(lives))

#Se puede hacer operatoria
lives = 12 + 15

#Se puede quitar uno al valor actual.
lives = lives - 1 
print(lives)
#forma rápida
lives -= 1

#Se puede multiplicar
lives = lives * 2
print(lives)
#forma rápida
lives *= 2

#Se puede dividir
lives = lives / 2
print(lives)
#forma rápida
lives /= 2

#Se puede elevar
lives = lives ** 2
print(lives)
#forma rápida
lives **= 2

#Se puede obtener el resto de una división
resto = 42 % 5
print(f'Resto: {resto}') 

#FLOAT
number = 3.5
print(number, type(number))

#Redondear
number = 7.5286554
print(number, type(number))
rounded_number = round(number,2)
print(rounded_number, type(rounded_number))

#Dejar un número con 2 cifras significativas
number = 0.00004528
number_str = format(number,'.2g')
print(number_str,type(number_str))