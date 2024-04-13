#Para detener un ciclo infinito con el teclado ctrl + c


#Tabla de multiplicar con while
contador = 1
y = int(input("numero de la tabla: "))
x = int(input("Ingresa hasta que numero quieres multiplicar : "))
while contador <= x:
    resultado = y * contador
    print(f"{y} X {contador} =  {resultado}");
    contador+= 1


counter = 0

while counter < 10:
  counter +=1
  print(counter)

counter2 = 0

#Se puede romper de manera forzada, por medio de un if y un break
while counter2 <10:
  counter2 +=1
  if counter2 == 7:
    break
  print(counter2)

counter3 = 0

#Si se escribe un if y un continue dentro, se salta el ciclo y continua con la siguiente iteración
while counter3 <10:
  counter3 +=1
  if counter3 < 5:
    continue
  print(counter3)

