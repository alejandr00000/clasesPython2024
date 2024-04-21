#07Cree un programa que pregunte por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
shopping_cart01 = input('Ingrese los productos del carrito de compras separados por comas: ')
shopping_cart02 = shopping_cart01.replace(',','\n')
print(shopping_cart02)