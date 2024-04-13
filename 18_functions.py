#Es frecuente utilizar algunas líneas de código de manera reiterada. En estos casos, 
#conviene escribirlas dentro de una función y luego llamar a la función cuando la necesitemos.
#Además, permite dar mayor legibilidad al código.

#Escribimos una función que sume dos valores, preguntando ambos al usuario.
a = float(input('Ingrese un primer número '))
b = float(input('Ingrese un segundo número '))

def suma(a, b):
    print(a, ' + ', b, ' = ',a + b)

suma(a,b)

#Crearemos una función que sumará los números enteros que se encuentren en un rango. 
#Retornará la suma.

print('La siguiente función sumará todos los números enteros en el rango indicado')

def sum_with_range(min, max):
    sum = 0
    for i in range (min,max+1):
        sum += i
    return sum

min = int(input('Ingrese el valor mínimo: '))
max = int(input('Ingrese el valor máximmo: '))
result = sum_with_range(min, max)
print(result)




