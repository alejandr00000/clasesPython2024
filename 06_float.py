#En los float, python usa una cierta cantidad de decimales (transformándolos a binario) y se generan errores en la operatoria.
x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print(x == y)

#".1f" deja una cirfa decinal. ".2g" deja dos cifras significativas.
y_str=format(y, ".1f")
print("str =>", y_str)
print(type(y_str))
print(y_str == str(x))

tolerance = 0.00001
print(abs(y - x) < tolerance)