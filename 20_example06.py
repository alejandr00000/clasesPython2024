#Se creará una función calculadora
input('La siguiente función realiza las cuatro operaciones matemáticas básicas entre dos números reales')

def calculator(num1, op, num2):
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    else: print('Error al ingresar los datos')
    return(result)

num1 = float(input('Ingrese el primer número: '))
op = input('Ingrese la operación que desea realizar. "+", "-", "*" o "/": ')
num2 = float(input('Ingrese el segundo número: '))

result = calculator(num1, op, num2)
print(result)