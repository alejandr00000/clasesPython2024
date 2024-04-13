pets = ['dog', 'cat', 'hamster','fish','other']
fav_pet = input(f'Ingrese su mascota favorita de la siguiente lista\n {pets}\n')

match fav_pet:
    case 'dog':
        print('Su mascota favorita es un perro.\n Tiene un buen gusto.')
    case 'cat':
        print('Su mascota favorita es un gato.\n.')
    case 'hamster':
        print('Su mascota favorita es un hamster')
    case 'fish':
        print('Su mascota favorita es un pez')
    case 'other':
        print('Su mascota favorita es otra')
    case _: 
        print('Error')


