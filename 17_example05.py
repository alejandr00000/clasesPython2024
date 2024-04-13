#Lista de países
countries = ['Argentina', 'Chile', 'Uruguay', 'Paraguay', 'Colombia', 'Venezuela', 'Bolivia']

#Se pide al usuario que ingrese un país. capitalize hace que sólo la primera letra 
#se transforme a mayúscula
search_country = input("Ingrese un país a buscar: ").capitalize()

#Comenzamos con una variable para saber si hemos encontrado el país. Al comienzo
#es False porque no lo hemos encontrado.
is_in_countries = False

'''
for country in countries:
    if country == search_country:
        print(f'El país {search_country} está en la lista. Se encuentra en la posición {countries.index(country)}')
        is_in_countries = True

if is_in_countries == False:
    print(f'Lo lamento. El país {search_country} no está en la lista')
'''

for i in range(0,len(countries)):
    if countries[i] == search_country:
        print(f'El país {search_country} está en la lista. Está en la pisición {i}')
        is_in_countries = True

if is_in_countries == False:
    print(f'Lo lamento. El país {search_country} no está en la lista')



