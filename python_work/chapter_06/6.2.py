# favorite_numbers = {
#     'livia': 1,
#     'maria': 2,
#     'jose': 3,
#     'bernardo': 4,
#     'celia': 5,
#     }

# for name, numeros in favorite_numbers.items():
#     print(f'O número favorito de {name.title()} é {numeros}!')

# Interação do usuário
favorite_numbers = {}

for i in range(5):
    name = input('Qual seu nome?\n')
    favorite_number = input('Qual seu número favorito?\n')
    favorite_numbers[name] = favorite_number

for name, number in favorite_numbers.items():
    print(f'O número favorito de {name.title()} é {number}!')