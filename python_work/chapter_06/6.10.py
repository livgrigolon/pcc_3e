favorite_numbers = {
    'livia': [1, 2, 3],
    'maria': [4, 5, 6],
    'bernardo': [7, 8, 9],
    }

# Unpacking (*)
for name, numbers in favorite_numbers.items():
    print(f"O(s) número(s) favorito(s) de {name.title()} é(são):", *numbers)

# Ou .join para formatar a saída de uma lista
for name, numbers in favorite_numbers.items():
    numeros_formatados = ', '.join(str(n) for n in numbers)
    print(f'O(s) número(s) favorito(s) de {name.title()} é(são): {numeros_formatados}!')

