pizzas = ['Pepperoni', 'Bacon', 'Mussarela', 'Queijos']

# for pizza in pizzas:
#     print(f'Gosto de pizza de {pizza}')

# print(f'Minha pizza favorita é de {pizzas[0]} \nMinha segunda pizza favorita é de {pizzas[1]} \nTambém gosto da pizza de {pizzas[2]}')
# print('Eu amo pizzas!')

friend_pizzas = pizzas[:]

pizzas.append('Calabresa')
friend_pizzas.append('Marguerita')

print(f'Minhas pizzas favoritas são:')
for pizza in pizzas:
    print(f'{pizza}')

print(f'Minhas pizzas favoritas são:')
for pizza in friend_pizzas:
    print(f'{pizza}')