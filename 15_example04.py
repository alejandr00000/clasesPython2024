#Lista de países
countries = ['Argentina', 'Chile', 'Uruguay', 'Paraguay', 'Colombia', 'Venezuela', 'Bolivia']

#Se pide al usuario que ingrese un país. capitalize hace que sólo la primera letra 
#se transforme a mayúscula
country = input("Ingrese un país a buscar: ").capitalize()

#Comenzamos con un contador y una variable para saber si hemos encontrado el país. Al comienzo
#es False porque no lo hemos encontrado.
counter = 0
is_in_countries = False
while counter < len(countries):
    if country == countries[counter]:
        is_in_countries = True
        print(f'El país {country} está en la lista. Se encuentra en la posición {counter}')
    counter = counter + 1

if is_in_countries == False:
    print(f'Lo lamento. El país {country} no está en la lista')



        
    